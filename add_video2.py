import os
import re

new_video_div = """<div style="display: flex; justify-content: center; width: 100%; flex-wrap: wrap; gap: 20px;">
                <iframe width="315" height="560" src="https://www.youtube.com/embed/toDtqobh2lc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); max-width: 100%;"></iframe>
                <iframe width="315" height="560" src="https://www.youtube.com/embed/Z-KCw7MdvYo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); max-width: 100%;"></iframe>
            </div>"""

def add_second_video(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match the old div that contains the single video
    old_div_pattern = re.compile(r'<div style="display: flex; justify-content: center; width: 100%;">\s*<iframe.*?</iframe>\s*</div>', re.DOTALL)
    
    if old_div_pattern.search(content):
        content = old_div_pattern.sub(new_video_div, content)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename} with 2nd video")
    else:
        # Maybe it's already updated, check if Z-KCw7MdvYo is there
        if "Z-KCw7MdvYo" not in content:
            print(f"Could not find video div in {filename}")
        else:
            print(f"Already updated {filename}")

add_second_video('sinov-laboratoriyasi.html')
add_second_video('sinov-laboratoriyasi_ru.html')
