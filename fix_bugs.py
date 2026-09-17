import os
import re

# Fix 1: Update script.js for the mobile menu bug
with open('js/script.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Make navBtn toggle conditional
js_content = js_content.replace(
    "navLinks.classList.toggle('active');\n        navBtn.classList.toggle('active');",
    "if(navLinks) navLinks.classList.toggle('active');\n        if(navBtn) navBtn.classList.toggle('active');"
)
with open('js/script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)


# Fix 2: Add .top-lang back to all missing files
uz_template = """<div class="top-lang">
                    <a href="{basename}" class="active">UZ</a> | <a href="{basename_ru}">RU</a>
                </div>"""
ru_template = """<div class="top-lang">
                    <a href="{basename_uz}">UZ</a> | <a href="{basename}" class="active">RU</a>
                </div>"""

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '<div class="top-lang">' not in content:
            # Figure out UZ and RU filenames
            if filename.endswith('_ru.html'):
                basename = filename
                basename_uz = filename.replace('_ru.html', '.html')
                lang_div = ru_template.format(basename=basename, basename_uz=basename_uz)
            else:
                basename = filename
                basename_ru = filename.replace('.html', '_ru.html')
                lang_div = uz_template.format(basename=basename, basename_ru=basename_ru)
            
            # Insert lang_div right after top-info
            content = re.sub(
                r'(<div class="top-info">.*?</div>)',
                r'\1\n                ' + lang_div,
                content,
                flags=re.DOTALL
            )
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)


# Fix 3: Fix inline font-size overflow on mobile in style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

css_content = css_content.replace(
    ".slide-content h1 {\n        font-size: 2rem;\n    }",
    ".slide-content h1 {\n        font-size: 2rem !important;\n        word-wrap: break-word;\n    }"
)

css_content = css_content.replace(
    ".slide-content h1 {\n        font-size: 1.6rem;\n    }",
    ".slide-content h1 {\n        font-size: 1.5rem !important;\n        word-wrap: break-word;\n    }"
)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("All fixes applied!")
