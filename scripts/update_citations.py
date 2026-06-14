import re
import sys
from scholarly import scholarly

SCHOLAR_ID = "1xA5KxAAAAAJ"
HTML_FILE = "index.html"

try:
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["basics"])
    citations = author["citedby"]
    print(f"Fetched citations: {citations}")
except Exception as e:
    print(f"Failed to fetch citations: {e}")
    sys.exit(1)

with open(HTML_FILE, "r", encoding="utf-8") as f:
    content = f.read()

updated = re.sub(
    r'(Total citations: <strong[^>]*>)\d+(</strong>)',
    rf'\g<1>{citations}\g<2>',
    content
)

if updated == content:
    print("No change detected.")
else:
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"Updated citations to {citations}")
