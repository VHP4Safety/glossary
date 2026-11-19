import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def plain(text):
    return re.sub(r'<[^>]+>|\s|"', "", text).casefold()


def assigned():
    with tempfile.NamedTemporaryFile("r") as output:
        subprocess.run([sys.executable, "scripts/assign_vhp_id.py"], env={**os.environ, "GITHUB_OUTPUT": output.name}, stdout=sys.stderr, check=True)
        return output.read().split("vhp_id=")[-1].strip()


terms = [json.loads(line) for line in open(sys.argv[1], encoding="utf-8")]
terms = [term for term in terms if term["draft"] and term["curator"] == sys.argv[2]]
known = "".join(path.read_text(encoding="utf-8") for path in Path("templates").glob("*.tsv")).casefold()
for path in sorted(Path("templates").glob("*.tsv")):
    rows = [line.split("\t") for line in path.read_text(encoding="utf-8").splitlines()]
    column = rows[0].index("contributor")
    for term in terms:
        if not term["id"] and term["table"] == path.stem and f"\t{term['term'].casefold()}\t" not in known:
            term["id"] = assigned()
            known += f"\t{term['term'].casefold()}\t"
            print(json.dumps({"iri": term["iri"], "id": term["id"]}))
            rows.append([term["id"]] + [""] * column)
        for row in rows:
            if row[0] == term["id"] and plain(row[1] + row[3]) != plain(term["term"] + term["definition"]):
                row += [""] * (column + 1 - len(row))
                row[1], row[3] = term["term"], term["definition"]
                row[column] = ",".join(dict.fromkeys(row[column].split(",") + term["contributors"])).strip(",")
    path.write_text("\n".join("\t".join(row) for row in rows) + "\n", encoding="utf-8")
