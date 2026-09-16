import os
import glob
import re

workspace = r"c:\Users\pc\OneDrive\Рабочий стол\project\sinpvss"
html_files = glob.glob(os.path.join(workspace, "*.html"))
html_files = [f for f in html_files if not f.endswith("_ru.html")]

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    filename = os.path.basename(filepath)
    ru_filename = filename.replace(".html", "_ru.html")
    
    new_lang = f'<div class="top-lang">\n                    <a href="{filename}" class="active">UZ</a> | <a href="{ru_filename}">RU</a>\n                </div>'
    
    content = re.sub(r'<div class="top-lang">.*?</div>', new_lang, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Language links updated in UZ files.")
