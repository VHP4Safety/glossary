import csv
import html
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

PLATFORM = sys.argv[2].rstrip("/") + "/"
HEADERS = {"Content-Type": "application/ld+json", "Accept": "application/ld+json", "Authorization": f"Bearer {os.environ['PLATFORM_TOKEN']}"}


def plain(text):
    return " ".join(html.unescape(re.sub(r"<[^>]+>", "", text)).split())


def send(method, path, body=None):
    request = urllib.request.Request(f"{PLATFORM}api/{path}", data=json.dumps(body).encode() if body else None, method=method, headers=HEADERS)
    with urllib.request.urlopen(request) as response:
        return json.load(response)


platform = {}
for line in open(sys.argv[1], encoding="utf-8"):
    term = json.loads(line)
    if not term["draft"]:
        platform[term["id"]] = term
for path in sorted(Path("templates").glob("*.tsv")):
    for row in list(csv.reader(open(path, encoding="utf-8"), delimiter="\t"))[1:]:
        if len(row) < 4 or not row[1].strip():
            continue
        name, description, address = plain(row[1]), plain(row[3]), f"https:/vhp4safety.github.io/glossary%23{row[0]}"
        if row[0] not in platform:
            send("POST", "terms", {"@id": f"https://vhp4safety.github.io/glossary#{row[0]}", "@type": "DefinedTerm", "termCode": row[0], "name": name,
                                   "description": description, "inDefinedTermSet": {"@id": f"{PLATFORM}vocabularies/vhp4safety-glossary"}})
            print("Added", row[0], name)
        elif (platform[row[0]]["term"], platform[row[0]]["definition"]) != (name, description):
            record = send("GET", address)
            record.pop("@context")
            record.update({"name": name, "description": description})
            send("PUT", address, record)
            print("Changed", row[0], name)
