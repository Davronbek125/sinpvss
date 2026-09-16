import re

file = 'narxlar.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace img tags in services to add lightbox
content = re.sub(
    r'<img src="img/(uslug\d\.jpg)" alt="Xizmatlar" style="width: 100%; height: 200px; object-fit: cover;">',
    r'<img src="img/\1" alt="Xizmatlar" style="width: 100%; height: 200px; object-fit: cover; cursor: zoom-in;" onclick="openLightbox(this.src)">',
    content
)

# Add script.js if not present
if 'script.js' not in content:
    content = content.replace('</body>', '    <script src="js/script.js"></script>\n</body>')

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated narxlar.html')
