import glob
import re

SUMMARY_TEXT = re.compile(r'<text[^>]*y="830"[^>]*>.*?</text>')
SUMMARY_ICON = re.compile(r'<g transform="translate\(\d+, 802\), scale\(2\)">.*?</g>')

for path in glob.glob("profile-3d-contrib/*.svg"):
    with open(path) as f:
        svg = f.read()
    stripped = SUMMARY_ICON.sub("", SUMMARY_TEXT.sub("", svg))
    with open(path, "w") as f:
        f.write(stripped)
