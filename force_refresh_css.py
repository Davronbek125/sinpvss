import os
import re

# Update HTML files to bust cache
for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = content.replace('css/style.css?v=2', 'css/style.css?v=3')
        if content != new_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)

# Update CSS file
with open('css/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

css_content = css_content.replace(
    "gap: 15px;",
    "gap: 25px;"
)

css_content = css_content.replace(
    "font-size: 1.1rem;",
    "font-size: 1.25rem;"
)

css_content = css_content.replace(
    "font-weight: 500;",
    "font-weight: 600;"
)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated CSS and HTML for cache busting!")
