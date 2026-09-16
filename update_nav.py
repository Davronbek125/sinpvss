import re

files = ['sertifikatlashtirish.html', 'sinov-laboratoriyasi.html', 'narxlar.html', 'index.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pages = {
        'index.html': 'Bosh sahifa',
        'sertifikatlashtirish.html': 'Sertifikatlashtirish',
        'sinov-laboratoriyasi.html': 'Sinov laboratoriyasi',
        'narxlar.html': 'Xizmatlar va narxlar',
        'hujjatlar.html': 'Hujjatlar va Ochiq ma\'lumotlar',
    }
    
    new_links = []
    for href, text in pages.items():
        if file == href:
            new_links.append(f'                    <li><a href="{href}" class="active">{text}</a></li>')
        else:
            new_links.append(f'                    <li><a href="{href}">{text}</a></li>')
            
    # Add contact link
    if file == 'index.html':
        new_links.append('                    <li><a href="#footer">Aloqa</a></li>')
    else:
        new_links.append('                    <li><a href="index.html#footer">Aloqa</a></li>')
            
    new_ul = '<ul class="nav-links">\n' + '\n'.join(new_links) + '\n                </ul>'
    
    content = re.sub(r'<ul class="nav-links">.*?</ul>', new_ul, content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {file}')
