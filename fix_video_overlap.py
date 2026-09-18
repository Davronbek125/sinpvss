import os
import re

script_code = """
<!-- YouTube IFrame API to pause other videos when one is played -->
<script src="https://www.youtube.com/iframe_api"></script>
<script>
    var players = [];
    
    // This function is called automatically by YouTube IFrame API
    function onYouTubeIframeAPIReady() {
        var iframes = document.querySelectorAll('.yt-video');
        iframes.forEach(function(iframe, index) {
            var player = new YT.Player(iframe, {
                events: {
                    'onStateChange': onPlayerStateChange
                }
            });
            players.push(player);
        });
    }

    function onPlayerStateChange(event) {
        if (event.data == YT.PlayerState.PLAYING) {
            var current_player = event.target;
            // Pause all other players
            players.forEach(function(player) {
                if (player !== current_player && typeof player.pauseVideo === 'function') {
                    player.pauseVideo();
                }
            });
        }
    }
</script>
</body>
"""

def fix_youtube_iframes(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add class="yt-video" and ?enablejsapi=1 to iframes
    # Pattern to match youtube embed urls
    content = re.sub(
        r'src="(https://www\.youtube\.com/embed/[^"]+)"',
        lambda m: f'src="{m.group(1)}?enablejsapi=1" class="yt-video"',
        content
    )

    # Clean up multiple classes or query params if already applied by accident
    content = content.replace('?enablejsapi=1?enablejsapi=1', '?enablejsapi=1')
    content = content.replace('class="yt-video" class="yt-video"', 'class="yt-video"')

    # 2. Add the script before </body>
    if '<script src="https://www.youtube.com/iframe_api"></script>' not in content:
        content = content.replace('</body>', script_code)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed videos in {filename}")

fix_youtube_iframes('sinov-laboratoriyasi.html')
fix_youtube_iframes('sinov-laboratoriyasi_ru.html')
