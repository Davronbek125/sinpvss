import urllib.request
import re

html = urllib.request.urlopen('https://www.sinovss.uz/').read().decode('utf-8')
match = re.search(r'<div class="logo">.*?</div>', html, re.DOTALL)
if match:
    print(match.group(0))
else:
    print("Logo div not found")
