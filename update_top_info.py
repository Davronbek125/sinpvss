import os
import re

uz_content = """<div class="top-info">
                    <span><i class="icon-clock"></i> Dushanba - Juma: 09:00 - 17:00 | Shanba: 09:00 - 14:00</span>
                    <span><i class="icon-phone"></i> +998 88 100 28 69, +998 99 335 07 70</span>
                    <span><i class="icon-email"></i> info@sinovss.uz</span>
                </div>"""

ru_content = """<div class="top-info">
                    <span><i class="icon-clock"></i> Пн - Пт: 09:00 - 17:00 | Сб: 09:00 - 14:00</span>
                    <span><i class="icon-phone"></i> +998 88 100 28 69, +998 99 335 07 70</span>
                    <span><i class="icon-email"></i> info@sinovss.uz</span>
                </div>"""

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        if filename.endswith('_ru.html'):
            new_content = re.sub(r'<div class="top-info">.*?</div>', ru_content, content, flags=re.DOTALL)
        else:
            new_content = re.sub(r'<div class="top-info">.*?</div>', uz_content, content, flags=re.DOTALL)
            
        if content != new_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
