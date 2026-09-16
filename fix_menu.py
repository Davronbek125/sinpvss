import os
import re

# Update HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add hamburger button if it doesn't exist
    if 'mobile-menu-btn' not in content:
        # Find logo and add button after it
        content = re.sub(
            r'(<div class="logo">.*?</div>)',
            r'\1\n                <button class="mobile-menu-btn">&#9776;</button>',
            content,
            flags=re.DOTALL
        )
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated HTML: {file}")

# Update script.js
with open('js/script.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

if 'mobile-menu-btn' not in js_content:
    js_addition = """
// Mobile Menu Logic
const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
const navLinks = document.querySelector('.nav-links');
const navBtn = document.querySelector('.nav-btn');

if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        navBtn.classList.toggle('active');
    });
}
"""
    with open('js/script.js', 'w', encoding='utf-8') as f:
        f.write(js_content + "\n" + js_addition)
    print("Updated js/script.js")

# Update style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if 'mobile-menu-btn' not in css_content:
    # Add desktop styles for mobile menu btn
    css_content = re.sub(
        r'(\.nav-btn \.btn \{[^}]+\})',
        r'\1\n\n/* Mobile Menu Button */\n.mobile-menu-btn {\n    display: none;\n    background: none;\n    border: none;\n    font-size: 1.8rem;\n    color: var(--primary-navy);\n    cursor: pointer;\n}',
        css_content
    )
    
    # Update max-width 992px
    old_992 = """.nav-inner {
        flex-direction: column;
        gap: 15px;
        padding: 10px 0;
    }
    .nav-links {
        flex-wrap: wrap;
        justify-content: center;
        gap: 10px 15px;
    }"""
    
    new_992 = """.nav-inner {
        flex-wrap: wrap;
        padding: 10px 15px;
    }
    .mobile-menu-btn {
        display: block;
    }
    .nav-links {
        display: none;
        width: 100%;
        flex-direction: column;
        text-align: center;
        gap: 10px;
        padding-top: 15px;
    }
    .nav-links.active {
        display: flex;
    }
    .nav-btn {
        display: none;
        width: 100%;
        text-align: center;
        margin-top: 10px;
    }
    .nav-btn.active {
        display: block;
    }"""
    
    css_content = css_content.replace(old_992, new_992)
    
    # In 480px, we can remove the nav-links flex-direction column since we already did it in 992px, 
    # but we will just leave it or overwrite it cleanly.
    old_480 = """.nav-links {
        flex-direction: column;
        width: 100%;
        text-align: center;
    }
    .nav-links li {
        width: 100%;
        padding: 8px 0;
        border-bottom: 1px solid #f1f5f9;
    }
    .nav-links li:last-child {
        border-bottom: none;
    }
    .nav-btn {
        width: 100%;
    }
    .nav-btn .btn {
        width: 100%;
    }"""
    
    new_480 = """.nav-links li {
        width: 100%;
        padding: 8px 0;
        border-bottom: 1px solid #f1f5f9;
    }
    .nav-links li:last-child {
        border-bottom: none;
    }
    .nav-btn .btn {
        width: 100%;
    }"""
    
    css_content = css_content.replace(old_480, new_480)
    
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("Updated css/style.css")
