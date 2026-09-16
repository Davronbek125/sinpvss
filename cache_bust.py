import os
import re

# 1. Clean up CSS
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# The duplicate mobile-menu-btn inside 480px media query starts around line 832.
# We can just remove the second occurrence or all occurrences of it and re-insert it cleanly.

css = re.sub(r'/\* Mobile Menu Button \*/\s*\.mobile-menu-btn\s*\{[^}]+\}', '', css)

# Now insert it cleanly ONCE after .nav-btn .btn
css = re.sub(
    r'(\.nav-btn \.btn\s*\{[^}]+\})',
    r'\1\n\n/* Mobile Menu Button */\n.mobile-menu-btn {\n    display: none;\n    background: none;\n    border: none;\n    font-size: 1.8rem;\n    color: var(--primary-navy);\n    cursor: pointer;\n}',
    css,
    count=1
)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("CSS cleaned up.")

# 2. Add cache buster to HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(r'href="css/style\.css(\?v=\d+)?"', 'href="css/style.css?v=2"', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Added cache buster to {file}")
