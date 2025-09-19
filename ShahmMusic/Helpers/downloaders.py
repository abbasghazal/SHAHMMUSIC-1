import os
from yt_dlp import YoutubeDL

COOKIES_PATH = os.path.join("cookies", "cookies.txt")

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(id)s.%(ext)s",
    "geo_bypass": True,
    "nocheckcertificate": True,
    "quiet": True,
    "no_warnings": True,
    "prefer_ffmpeg": True,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        }
    ],
}

if os.path.exists(COOKIES_PATH):
    ydl_opts["cookiefile"] = COOKIES_PATH

ydl = YoutubeDL(ydl_opts)

def audio_dl(url: str) -> str:
    sin = ydl.extract_info(url, False)
    x_file = os.path.join("downloads", f"{sin['id']}.mp3")
    if os.path.exists(x_file):
        return x_file
    ydl.download([url])
    return x_file

def setup_cookies_directory():
    cookies_dir = "cookies"
    if not os.path.exists(cookies_dir):
        os.makedirs(cookies_dir)
    cookies_file = os.path.join(cookies_dir, "cookies.txt")
    if not os.path.exists(cookies_file):
        with open(cookies_file, 'w') as f:
            f.write("# ملف الكوكيز\n# أضف الكوكيز هنا بتنسيق Netscape\n")

setup_cookies_directory()
