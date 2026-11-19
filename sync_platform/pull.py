import json
import re
import sys
import urllib.request

PLATFORM = sys.argv[1].rstrip("/") + "/"


def listed(kind, query=""):
    found, page = [], 1
    while page:
        request = urllib.request.Request(f"{PLATFORM}api/{kind}?page_size=48&page={page}{query}", headers={"Accept": "application/ld+json"})
        with urllib.request.urlopen(request) as response:
            found += json.load(response)["@graph"]
            page = json.loads(response.headers["X-Pagination"]).get("next_page")
    return found


people = {}
for person in listed("people"):
    links = json.dumps(person.get("sameAs"))
    people[person["@id"]] = re.findall(r"https://orcid\.org/[\dX-]+", links)[:1] + re.findall(r"https://github\.com/[\w-]+", links)[:1]
for term in listed("terms", f"&inDefinedTermSet={PLATFORM}vocabularies/vhp4safety-glossary"):
    contributors = [people.get(iri) or [iri] for iri in re.findall(r'"@id": "([^"]+)"', json.dumps(term.get("dct:contributor")))]
    curators = re.findall(r"https://github\.com/([\w-]+)", json.dumps(contributors))
    print(json.dumps({"iri": term["@id"], "id": term.get("termCode", ""), "table": term.get("term:glossaryTable", ""), "term": term.get("name", ""), "definition": term.get("description", ""),
                      "draft": term.get("creativeWorkStatus") == "Draft", "curator": curators[-1] if curators else "", "contributors": [person[0] for person in contributors]}))
