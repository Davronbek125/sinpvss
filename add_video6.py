import os

new_iframe = '\n                <iframe width="315" height="560" src="https://www.youtube.com/embed/qtjn8gHC-wg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); max-width: 100%;"></iframe>'

def add_sixth_video(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    if '</iframe>\n            </div>' in content:
        content = content.replace('</iframe>\n            </div>', f'</iframe>{new_iframe}\n            </div>')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename} with 6th video")
    else:
        print(f"Could not find video div in {filename}")

add_sixth_video('sinov-laboratoriyasi.html')
add_sixth_video('sinov-laboratoriyasi_ru.html')
