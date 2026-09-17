import os
import re

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace img/logo.png with img/logo.jpg and height: 50px to 90px
        new_content = re.sub(
            r'<img src="img/logo\.png" alt="SINOV SERTIFIQAT SERVIS" style="height: \d+px;">',
            r'<img src="img/logo.jpg" alt="SINOV SERTIFIQAT SERVIS" style="height: 90px;">',
            content,
            flags=re.IGNORECASE
        )

        if content != new_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
