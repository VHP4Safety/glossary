import re
import subprocess
from pathlib import Path


def run(*arguments):
    return subprocess.run(arguments, capture_output=True, text=True).stdout.strip()


tables = {path: [line.split("\t") for line in path.read_text(encoding="utf-8").splitlines() if line.strip()] for path in sorted(Path("templates").glob("*.tsv"))}
labels = {row[1].strip().casefold(): row[0] for rows in tables.values() for row in rows[1:]}
first, sha = {}, None
for line in run("git", "log", "--reverse", "--no-merges", "-p", "--format=commit %H", "--", "templates", "glossary.md", "index.md").splitlines():
    if line.startswith("commit "):
        sha = line.removeprefix("commit ")
    elif line.startswith("+"):
        for cell in re.split(r"[|\t<>]", line[1:]) + re.findall(r"VHP\d{7}", line):
            first.setdefault(labels.get(cell.strip().casefold(), cell), sha)
edits = {}
for commit in run("git", "log", "--reverse", "--no-merges", "-p", "--unified=0", "--format=%x00%H", "--", "templates").split("\0")[1:]:
    sha, *lines = commit.splitlines()
    removed = {line[1:].split("\t")[0]: [cell.strip() for cell in line[1:].split("\t")[:4]] for line in lines if line.startswith("-VHP")}
    for line in lines:
        cells = [cell.strip() for cell in line[1:].split("\t")[:4]]
        if line.startswith("+VHP") and removed.get(cells[0], cells) != cells:
            edits.setdefault(cells[0], []).append(sha)
requesters = {}
for line in run("gh", "api", "--paginate", "repos/VHP4Safety/glossary/issues?state=all&per_page=100", "--jq",
                '.[] | select(.pull_request == null and (.title | contains("[TERM REQUEST]"))) | "\\(.number) \\(.user.login)"').splitlines():
    number, login = line.split()
    comments = run("gh", "api", "--paginate", f"repos/VHP4Safety/glossary/issues/{number}/comments?per_page=100", "--jq", ".[].body")
    for identifier in re.findall(r"VHP Identifier Assigned:\*\*\s*`(VHP\d{7})`", comments):
        requesters.setdefault(identifier, login)
logins = {None: None}
for path, rows in tables.items():
    rows[0].append("contributor")
    for row in rows[1:]:
        given = [requesters.get(row[0])]
        for sha in [first.get(row[0])] + edits.get(row[0], []):
            if sha not in logins:
                login = run("gh", "api", f"repos/VHP4Safety/glossary/commits/{sha}", "--jq", ".author.login // empty")
                logins[sha] = run("gh", "api", f"repos/VHP4Safety/glossary/commits/{sha}/pulls", "--jq", ".[0].user.login // empty") if login.endswith("[bot]") else login
            given.append(logins[sha])
        links = [f"https://github.com/{login}" for login in given if login]
        row += [""] * (len(rows[0]) - 1 - len(row)) + [",".join(dict.fromkeys(links))]
    path.write_text("\n".join("\t".join(row) for row in rows) + "\n", encoding="utf-8")
