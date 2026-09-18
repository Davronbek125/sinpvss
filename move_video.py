import os
import re

def move_video_section(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match the video section
    video_pattern = re.compile(r'(\s*<!-- Video Section -->\s*<section.*?</section>\s*)', re.DOTALL)
    video_match = video_pattern.search(content)
    
    if not video_match:
        print(f"Video section not found in {filename}")
        return
        
    video_block = video_match.group(1)
    
    # Remove video block from its current place
    content = content.replace(video_block, '\n')
    
    # Find the end of Lab & Accreditation Gallery
    gallery_pattern = re.compile(r'(<!-- Lab & Accreditation Gallery -->.*?</section>)', re.DOTALL)
    gallery_match = gallery_pattern.search(content)
    
    if gallery_match:
        gallery_block = gallery_match.group(1)
        # Insert video block right after gallery block
        content = content.replace(gallery_block, gallery_block + video_block)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Moved video section in {filename}")
    else:
        print(f"Gallery section not found in {filename}")

move_video_section('sinov-laboratoriyasi.html')
move_video_section('sinov-laboratoriyasi_ru.html')
