import base64, datetime, glob, json, math, os, subprocess, sys, tempfile
from xml.sax.saxutils import escape
from fontTools.ttLib import TTFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC = os.environ.get("STATIC") == "1"
OUT = os.path.join(ROOT, "preview" if STATIC else "cards")
cfg = json.load(open(os.path.join(ROOT, "config.json")))
data = json.load(open(os.path.join(ROOT, "data", "contributions.json")))
C = cfg["colors"]
W = 830

FONTS = {
    "d7": ("GS", 700, "general-sans-700.woff2"),
    "d6": ("GS", 600, "general-sans-600.woff2"),
    "d5": ("GS", 500, "general-sans-500.woff2"),
    "b4": ("CG", 400, "cabinet-grotesk-400.woff2"),
    "b5": ("CG", 500, "cabinet-grotesk-500.woff2"),
}
_ttf = {}
_subset_cache = {}


def ttf(key):
    if key not in _ttf:
        _ttf[key] = TTFont(os.path.join(ROOT, "assets", "fonts", FONTS[key][2]))
    return _ttf[key]


def measure(text, key, size):
    f = ttf(key)
    cmap, hmtx, upm = f.getBestCmap(), f["hmtx"], f["head"].unitsPerEm
    total = sum(hmtx[cmap[ord(c)]][0] if ord(c) in cmap else upm * 0.55 for c in text)
    return total / upm * size


def wrap(text, key, size, maxw, maxlines):
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if measure(trial, key, size) <= maxw or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    lines.append(cur)
    if len(lines) > maxlines:
        lines = lines[:maxlines]
        while measure(lines[-1] + "...", key, size) > maxw:
            lines[-1] = lines[-1].rsplit(" ", 1)[0] if " " in lines[-1] else lines[-1][:-1]
        lines[-1] += "..."
    return lines


def subset_b64(key, chars):
    ck = (key, "".join(sorted(chars)))
    if ck not in _subset_cache:
        src = os.path.join(ROOT, "assets", "fonts", FONTS[key][2])
        with tempfile.TemporaryDirectory() as td:
            dst = os.path.join(td, "s.woff2")
            subprocess.run(
                [sys.executable, "-m", "fontTools.subset", src, f"--text={''.join(sorted(chars))}",
                 "--flavor=woff2", "--layout-features=kern", f"--output-file={dst}"],
                check=True, capture_output=True)
            _subset_cache[ck] = base64.b64encode(open(dst, "rb").read()).decode()
    return _subset_cache[ck]


def mix(a, b, t):
    pa = [int(a[i:i + 2], 16) for i in (1, 3, 5)]
    pb = [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * t):02x}" for x, y in zip(pa, pb))


def fmt(n):
    return f"{n:,}"


ARROW = "M0 8h12M7 3l5 5-5 5"
STAR = ("M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97"
        ".719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194"
        "L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z")
FORK = ("M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878"
        "a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25"
        "v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 "
        "0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z")

BASE_CSS = f"""
text{{font-family:CG,'Helvetica Neue',Arial,sans-serif}}
.d7,.d6,.d5{{font-family:GS,'Helvetica Neue',Arial,sans-serif}}
.d7{{font-weight:700}}.d6{{font-weight:600}}.d5{{font-weight:500}}
.b4{{font-weight:400}}.b5{{font-weight:500}}
"""
ANIM_CSS = """
.rise{animation:rise .8s cubic-bezier(.2,.7,.2,1) var(--d,0s) both}
.fade{animation:fade .8s ease var(--d,0s) both}
.pop{transform-box:fill-box;transform-origin:center;animation:pop .5s cubic-bezier(.2,.9,.3,1.2) var(--d,0s) both}
.growy{transform-box:fill-box;transform-origin:50% 100%;animation:growy .9s cubic-bezier(.2,.7,.2,1) var(--d,0s) both}
.growx{transform-box:fill-box;transform-origin:0 50%;animation:growx .9s cubic-bezier(.2,.7,.2,1) var(--d,0s) both}
@keyframes rise{from{opacity:0;transform:translateY(10px)}}
@keyframes fade{from{opacity:0}}
@keyframes pop{from{opacity:0;transform:scale(.4)}}
@keyframes growy{from{transform:scaleY(0)}}
@keyframes growx{from{transform:scaleX(0)}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}.fx{display:none}}
"""


class Card:
    def __init__(self, name, w, h, delay, label):
        self.name, self.w, self.h, self.delay, self.label = name, w, h, delay, label
        self.parts, self.chars = [], {}

    def style(self, d):
        return "" if STATIC else f' style="--d:{self.delay + d:.2f}s"'

    def add(self, s):
        self.parts.append(s)

    def text(self, x, y, s, font, size, fill, anchor="start", d=0.0, anim="rise", ls=0):
        self.chars.setdefault(font, set("0123456789 .,")).update(s)
        cls = f"{font} {anim}" if not STATIC else font
        a = f' text-anchor="{anchor}"' if anchor != "start" else ""
        l = f' letter-spacing="{ls}"' if ls else ""
        self.add(f'<text x="{x}" y="{y}" class="{cls}" font-size="{size}" fill="{fill}"{a}{l}{self.style(d)}>{escape(s)}</text>')

    def el(self, markup, anim, d=0.0):
        if STATIC or not anim:
            self.add(markup)
        else:
            self.add(f'<g class="{anim}"{self.style(d)}>{markup}</g>')

    def fx(self, markup):
        if not STATIC:
            self.add(f'<g class="fx">{markup}</g>')

    def render(self):
        faces = "".join(
            f"@font-face{{font-family:{FONTS[k][0]};font-weight:{FONTS[k][1]};"
            f"src:url(data:font/woff2;base64,{subset_b64(k, ch)}) format('woff2')}}"
            for k, ch in sorted(self.chars.items()))
        css = faces + BASE_CSS + ("" if STATIC else ANIM_CSS)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
                f'viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{escape(self.label)}">'
                f'<style>{css}</style>{"".join(self.parts)}</svg>\n')


def frame(c, rx=18):
    c.add(f'<rect x=".5" y=".5" width="{c.w - 1}" height="{c.h - 1}" rx="{rx}" fill="{C["ink"]}" stroke="{C["line"]}"/>')


def find_portrait():
    for p in sorted(glob.glob(os.path.join(ROOT, "assets", "portrait.*"))):
        ext = p.rsplit(".", 1)[1].lower()
        mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}.get(ext)
        if mime:
            raw = open(p, "rb").read()
            if len(raw) > 150_000:
                print(f"warning: {os.path.basename(p)} is {len(raw) // 1000}KB, shrink it", file=sys.stderr)
            return f"data:image/{mime};base64," + base64.b64encode(raw).decode()
    return None


def hero():
    h = 250
    c = Card("hero", W, h, 0.0, f"{cfg['name']}. {cfg['tagline']}")
    portrait = find_portrait()
    c.add(f'<defs><radialGradient id="g" cx="85%" cy="20%" r="70%"><stop offset="0" stop-color="{C["brand"]}" stop-opacity=".28"/>'
          f'<stop offset="1" stop-color="{C["brand"]}" stop-opacity="0"/></radialGradient>'
          f'<linearGradient id="sh" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
          f'<stop offset=".5" stop-color="#fff" stop-opacity=".07"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
          f'<clipPath id="r"><rect width="{W}" height="{h}" rx="18"/></clipPath>'
          f'<clipPath id="p"><circle cx="{W - 140}" cy="{h / 2}" r="72"/></clipPath></defs>')
    frame(c)
    c.add(f'<rect width="{W}" height="{h}" rx="18" fill="url(#g)"/>')
    avail = (W - 140 - 80 - 48 - 32) if portrait else W - 96
    size = min(54, 54 * avail / measure(cfg["name"], "d7", 54))
    c.text(48, 70, "SOFTWARE ENGINEER II", "d6", 13, C["brand"], d=0.1, ls=2.6)
    c.text(48, 70 + size + 12, cfg["name"], "d7", round(size, 1), C["cream"], d=0.25)
    ry = 70 + size + 36
    c.el(f'<rect x="48" y="{ry}" width="72" height="3" rx="1.5" fill="{C["brand"]}"/>', "growx", 0.5)
    for i, line in enumerate(wrap(cfg["tagline"], "b4", 21, avail, 2)):
        c.text(48, ry + 42 + i * 30, line, "b4", 21, C["bone"], d=0.65 + i * 0.1)
    if portrait:
        cx, cy = W - 140, h / 2
        c.el(f'<circle cx="{cx}" cy="{cy}" r="80" fill="none" stroke="{C["brand"]}" stroke-width="2" stroke-opacity=".6"/>'
             f'<image href="{portrait}" x="{cx - 72}" y="{cy - 72}" width="144" height="144" preserveAspectRatio="xMidYMid slice" clip-path="url(#p)"/>',
             "pop", 0.4)
    c.fx(f'<g clip-path="url(#r)"><rect x="-300" y="0" width="300" height="{h}" fill="url(#sh)">'
         f'<animateTransform attributeName="transform" type="translate" from="0 0" to="{W + 300} 0" '
         f'begin="{0.5}s" dur="1.8s" fill="freeze"/></rect></g>')
    return c


def tile(i, t):
    w, h = 270, 112
    c = Card(f"tile-{i + 1}", w, h, 0.7 + 0.12 * i, f"{t['title']}: {t['sub']}")
    frame(c, 16)
    c.add(f'<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="16" fill="none" stroke="{C["brand"]}" stroke-opacity=".35"/>')
    c.text(22, 34, t["label"], "d6", 11, C["brand"], d=0.0, ls=2)
    size = min(24, 24 * (w - 44 - 28) / measure(t["title"], "d6", 24))
    c.text(22, 66, t["title"], "d6", round(size, 1), C["cream"], d=0.1)
    c.text(22, 90, t["sub"], "b4", 14, C["sage"], d=0.2)
    arrow = f'<path d="{ARROW}" fill="none" stroke="{C["cream"]}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
    nudge = ('<animateTransform attributeName="transform" type="translate" values="0 0;4 0;0 0" dur="2.4s" '
             'begin="1.5s" repeatCount="indefinite"/>')
    c.el(f'<g transform="translate({w - 40} {26})"><g>{arrow}{"" if STATIC else nudge}</g></g>', "fade", 0.3)
    return c


def stats(days):
    last = datetime.date.fromisoformat(days[-1]["date"])
    counts = [d["count"] for d in days]
    i = len(counts) - 1
    if counts[i] == 0:
        i -= 1
    streak = 0
    while i >= 0 and counts[i] > 0:
        streak += 1
        i -= 1
    year = days[-365:]
    active = sum(1 for d in year if d["count"] > 0)
    best = max(year, key=lambda d: d["count"])
    months = []
    y, m = last.year, last.month
    for _ in range(12):
        months.append((y, m))
        m -= 1
        if m == 0:
            y, m = y - 1, 12
    months.reverse()
    monthly = [sum(d["count"] for d in days if d["date"].startswith(f"{y}-{m:02d}")) for y, m in months]
    return last, streak, active, len(year), best, months, monthly


def activity():
    days = data["days"]
    last, streak, active, span, best, months, monthly = stats(days)
    h = 345
    c = Card("activity", W, h, 1.4, f"Contributions per month. Streak {streak} days, {active} active days.")
    frame(c)
    year_total = sum(d["count"] for d in days[-365:])
    c.text(36, 50, "Contributions", "d6", 22, C["cream"], d=0.0)
    c.text(W - 36, 50, f"{fmt(year_total)} in the last year", "b4", 15, C["sage"], anchor="end", d=0.1)
    c.add(f'<line x1="250" y1="84" x2="250" y2="{h - 36}" stroke="{C["line"]}"/>')
    bd = datetime.date.fromisoformat(best["date"])
    blocks = [
        ("CURRENT STREAK", str(streak), "days" if streak != 1 else "day"),
        ("ACTIVE DAYS", str(active), f"of the last {span} days"),
        ("BUSIEST DAY", str(best["count"]), f"{bd.strftime('%b')} {bd.day}, {bd.year}"),
    ]
    for i, (lab, val, sub) in enumerate(blocks):
        y = 92 + i * 82
        d = 0.2 + i * 0.15
        c.text(36, y, lab, "d6", 11, C["brand"], d=d, ls=2)
        c.text(36, y + 38, val, "d7", 40, C["cream"], d=d + 0.05)
        c.text(36 + measure(val, "d7", 40) + 10, y + 38, sub, "b4", 14, C["sage"], d=d + 0.1)
    dx = 36 + measure(blocks[0][0], "d6", 11) + 2 * len(blocks[0][0]) + 8
    c.el(f'<circle cx="{dx}" cy="{92 - 4}" r="4" fill="{C["brand"]}"/>', "fade", 0.3)
    c.fx(f'<circle cx="{dx}" cy="{92 - 4}" r="4" fill="none" stroke="{C["brand"]}" stroke-width="1.5" stroke-opacity="0">'
         f'<animate attributeName="r" values="4;13" dur="2.2s" begin="1.6s" repeatCount="indefinite"/>'
         f'<animate attributeName="stroke-opacity" values=".7;0" dur="2.2s" begin="1.6s" repeatCount="indefinite"/></circle>')
    x0, slot, base, top = 285, 42.4, 290, 140
    mx = max(monthly) or 1
    for g in range(4):
        gy = base - (base - top) * g / 3
        c.el(f'<line x1="{x0 - 8}" y1="{gy:.1f}" x2="{W - 30}" y2="{gy:.1f}" stroke="{C["line"]}" stroke-dasharray="{"0" if g == 0 else "2 4"}"/>', "fade", 0.2)
    peak = monthly.index(max(monthly))
    for i, ((y, m), v) in enumerate(zip(months, monthly)):
        bx = x0 + i * slot + (slot - 26) / 2
        bh = max(2, (base - top) * v / mx)
        col = C["sage"] if i == peak else C["brand"]
        d = 0.35 + i * 0.07
        c.el(f'<rect x="{bx:.1f}" y="{base - bh:.1f}" width="26" height="{bh:.1f}" rx="5" fill="{col}"/>', "growy", d)
        c.text(round(bx + 13, 1), round(base - bh - 8, 1), fmt(v), "b5", 11.5, C["cream"] if i == peak else C["bone"], anchor="middle", d=d + 0.5)
        c.text(round(bx + 13, 1), base + 24, datetime.date(y, m, 1).strftime("%b"), "b4", 12, C["sage"], anchor="middle", d=d + 0.1)
    return c


def repo(i, r):
    h = 150
    c = Card(f"repo-{i + 1}", W, h, 2.3 + 0.3 * i, f"{r['name']}: {r['description']}")
    frame(c)
    c.el(f'<rect x="0" y="22" width="4" height="{h - 44}" rx="2" fill="{C["brand"]}"/>', "growy", 0.0)
    c.text(36, 46, f"{cfg['login']} /", "b5", 15, C["mute"], d=0.1)
    nx = 36 + measure(f"{cfg['login']} /", "b5", 15) + 8
    c.text(round(nx, 1), 46, r["name"], "d6", 22, C["cream"], d=0.15)
    c.el(f'<g transform="translate({W - 56} 32)"><path d="{ARROW}" fill="none" stroke="{C["sage"]}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></g>', "fade", 0.3)
    for k, line in enumerate(wrap(r["description"] or "No description yet.", "b4", 15.5, W - 72, 2)):
        c.text(36, 76 + k * 22, line, "b4", 15.5, C["bone"], d=0.25 + k * 0.08)
    x, fy = 36, h - 26
    d = 0.5
    if r["language"]:
        c.el(f'<circle cx="{x + 5}" cy="{fy - 5}" r="5" fill="{r["color"]}"/>', "pop", d)
        c.text(x + 17, fy, r["language"], "b5", 13, C["sage"], d=d)
        x += 17 + measure(r["language"], "b5", 13) + 26
    for icon, n in ((STAR, r["stars"]), (FORK, r["forks"])):
        c.el(f'<path transform="translate({x} {fy - 12}) scale(.8)" d="{icon}" fill="{C["sage"]}"/>', "fade", d + 0.1)
        c.text(x + 20, fy, str(n), "b5", 13, C["sage"], d=d + 0.1)
        x += 20 + measure(str(n), "b5", 13) + 24
    return c


def graph():
    days = data["days"]
    h = 236
    c = Card("graph", W, h, 3.3, "Contribution graph for the last year")
    frame(c)
    c.text(36, 46, "Contribution graph", "d6", 22, C["cream"], d=0.0)
    c.text(W - 36, 46, "last 12 months", "b4", 15, C["sage"], anchor="end", d=0.1)
    nz = sorted(d["count"] for d in days if d["count"] > 0)
    q = [nz[int(len(nz) * p)] for p in (0.25, 0.5, 0.75)] if nz else [1, 2, 3]
    shades = [mix(C["panel"], C["brand"], 0.08)] + [mix(C["panel"], C["brand"], t) for t in (0.4, 0.7)] + [C["brand"], mix(C["brand"], C["cream"], 0.45)]

    def level(n):
        return 0 if n == 0 else 1 + sum(n > t for t in q)

    gx, gy, pitch, cell = 52, 84, 14, 11
    weeks = [days[i:i + 7] for i in range(0, len(days), 7)]
    prev_m, last_lab = None, -9
    for wi, wk in enumerate(weeks):
        x = gx + wi * pitch
        mo = wk[0]["date"][5:7]
        if mo != prev_m and wi - last_lab > 2:
            c.text(x, gy - 10, datetime.date.fromisoformat(wk[0]["date"]).strftime("%b"), "b4", 11, C["sage"], d=0.2 + wi * 0.02)
            last_lab = wi
        prev_m = mo
        cells = "".join(
            f'<rect x="{x}" y="{gy + k * pitch}" width="{cell}" height="{cell}" rx="2.5" fill="{shades[level(d["count"])]}"/>'
            for k, d in enumerate(wk))
        c.el(f"<g>{cells}</g>", "fade", 0.25 + wi * 0.035)
    for k, name in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        c.text(gx - 10, gy + k * pitch + 9, name, "b4", 10.5, C["mute"], anchor="end", d=0.2)
    li = len(weeks) - 1
    lk = len(weeks[-1]) - 1
    if not STATIC:
        px, py = gx + li * pitch + cell / 2, gy + lk * pitch + cell / 2
        c.fx(f'<circle cx="{px}" cy="{py}" r="6" fill="none" stroke="{C["cream"]}" stroke-width="1.2" stroke-opacity="0">'
             f'<animate attributeName="r" values="6;14" dur="2.2s" begin="{0.25 + li * 0.035 + 1}s" repeatCount="indefinite"/>'
             f'<animate attributeName="stroke-opacity" values=".8;0" dur="2.2s" begin="{0.25 + li * 0.035 + 1}s" repeatCount="indefinite"/></circle>')
    ly = h - 28
    lx = W - 36
    c.text(lx, ly + 9, "More", "b4", 11, C["sage"], anchor="end", d=1.0)
    lx -= measure("More", "b4", 11) + 8
    for s in reversed(shades):
        lx -= cell
        c.el(f'<rect x="{lx}" y="{ly}" width="{cell}" height="{cell}" rx="2.5" fill="{s}"/>', "fade", 1.0)
        lx -= 4
    c.text(lx - 4, ly + 9, "Less", "b4", 11, C["sage"], anchor="end", d=1.0)
    return c


def main():
    os.makedirs(OUT, exist_ok=True)
    cards = [hero()] + [tile(i, t) for i, t in enumerate(cfg["tiles"])] + [activity()]
    cards += [repo(i, r) for i, r in enumerate(data["repos"])] + [graph()]
    for c in cards:
        with open(os.path.join(OUT, f"{c.name}.svg"), "w") as f:
            f.write(c.render())
    if STATIC:
        tiles = "".join(f'<img src="tile-{i + 1}.svg" width="32.5%">' for i in range(len(cfg["tiles"])))
        rows = "".join(f'<p><img src="{c.name}.svg" width="100%"></p>' for c in cards if c.name.split("-")[0] in ("hero", "activity", "repo", "graph"))
        html = rows.replace(f'<p><img src="activity.svg"', f'<p>{tiles}</p><p><img src="activity.svg"', 1)
        open(os.path.join(OUT, "index.html"), "w").write(
            f'<body style="margin:0;padding:24px;background:#fff;max-width:830px;margin:auto">{html}</body>')
    print(f"{len(cards)} cards -> {os.path.relpath(OUT, ROOT)}{' (static)' if STATIC else ''}")


main()
