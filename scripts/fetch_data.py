import json, os, re, sys, urllib.request, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cfg = json.load(open(os.path.join(ROOT, "config.json")))
token = os.environ.get("GITHUB_TOKEN")
if not token:
    sys.exit("GITHUB_TOKEN is not set")

def gql(query, variables=None):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables or {}}).encode(),
        headers={"Authorization": f"bearer {token}", "User-Agent": "profile-cards"},
    )
    out = json.load(urllib.request.urlopen(req, timeout=30))
    if out.get("errors"):
        sys.exit(json.dumps(out["errors"]))
    return out["data"]

cal = gql(
    "query($l:String!){user(login:$l){contributionsCollection{contributionCalendar{"
    "totalContributions weeks{contributionDays{date contributionCount}}}}}}",
    {"l": cfg["login"]},
)["user"]["contributionsCollection"]["contributionCalendar"]
days = [
    {"date": d["date"], "count": d["contributionCount"]}
    for w in cal["weeks"] for d in w["contributionDays"]
]

fields = "name description url stargazerCount forkCount primaryLanguage{name color}"
parts = []
for i, name in enumerate(cfg["featured"]):
    if not re.fullmatch(r"[\w.-]+", name):
        sys.exit(f"bad repo name {name}")
    parts.append(f'r{i}:repository(owner:"{cfg["login"]}",name:"{name}"){{{fields}}}')
raw = gql("{" + " ".join(parts) + "}")
repos = []
for i, name in enumerate(cfg["featured"]):
    r = raw[f"r{i}"]
    if r is None:
        sys.exit(f"repo not found: {name}")
    lang = r["primaryLanguage"] or {}
    repos.append({
        "name": r["name"], "description": r["description"] or "", "url": r["url"],
        "stars": r["stargazerCount"], "forks": r["forkCount"],
        "language": lang.get("name", ""), "color": lang.get("color") or "#8c8c73",
    })

out = {
    "generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "login": cfg["login"], "total": cal["totalContributions"], "days": days, "repos": repos,
}
with open(os.path.join(ROOT, "data", "contributions.json"), "w") as f:
    json.dump(out, f, indent=1)
    f.write("\n")
print(f"{len(days)} days, total {out['total']}, {len(repos)} repos")
