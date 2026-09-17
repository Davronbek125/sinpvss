import os
import re

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace text logo with image logo for index.html links
        new_content = re.sub(
            r'<div class="logo">\s*<a href="(index[^"]*\.html)">\s*<strong>SINOV SERTIFIQAT SERVIS</strong>\s*</a>\s*</div>',
            r'<div class="logo">\n                    <a href="\1">\n                        <img src="img/logo.png" alt="SINOV SERTIFIQAT SERVIS" style="height: 50px;">\n                    </a>\n                </div>',
            content,
            flags=re.IGNORECASE
        )

        if content != new_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
