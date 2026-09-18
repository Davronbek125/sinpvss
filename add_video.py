import os

uz_video_section = """
    <!-- Video Section -->
    <section style="padding: 40px 0; background: var(--bg-white);">
        <div class="container text-center">
            <h2 class="section-title">Laboratoriya jarayonidan lavha</h2>
            <div style="display: flex; justify-content: center; width: 100%;">
                <iframe width="315" height="560" src="https://www.youtube.com/embed/toDtqobh2lc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); max-width: 100%;"></iframe>
            </div>
        </div>
    </section>

"""

ru_video_section = """
    <!-- Video Section -->
    <section style="padding: 40px 0; background: var(--bg-white);">
        <div class="container text-center">
            <h2 class="section-title">Видео процесса работы лаборатории</h2>
            <div style="display: flex; justify-content: center; width: 100%;">
                <iframe width="315" height="560" src="https://www.youtube.com/embed/toDtqobh2lc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); max-width: 100%;"></iframe>
            </div>
        </div>
    </section>

"""

def insert_video(filename, video_html):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "<!-- Video Section -->" in content:
        print(f"Video already embedded in {filename}")
        return

    content = content.replace("<!-- Lab & Accreditation Gallery -->", video_html + "    <!-- Lab & Accreditation Gallery -->")
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

insert_video('sinov-laboratoriyasi.html', uz_video_section)
insert_video('sinov-laboratoriyasi_ru.html', ru_video_section)
