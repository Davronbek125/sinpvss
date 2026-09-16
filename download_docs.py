import urllib.request
import urllib.parse
import os

files = ["2-УТВЕРЖДАЮ.docx", "3-УТВЕРЖДАЮ.docx", "4-УТВЕРЖДАЮ.docx"]
out = ["2-narx.docx", "3-narx.docx", "4-narx.docx"]

os.makedirs("docs", exist_ok=True)
for f, o in zip(files, out):
    url = "https://www.sinovss.uz/docs/" + urllib.parse.quote(f)
    print("Downloading", url)
    try:
        urllib.request.urlretrieve(url, "docs/" + o)
        print("Success for", o)
    except Exception as e:
        print("Failed for", o, e)
print("Done")
