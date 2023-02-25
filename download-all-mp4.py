#!python3

from __future__ import unicode_literals

import os
from pathlib import Path

import console
from pytube import YouTube

outdir = os.path.expanduser("~/Documents/Downloads")
try:
    os.mkdir(outdir)
except FileExistsError:
    pass


def download_video(url):
    yt = YouTube(url)
    print("🏎 Starting download of", yt.title)
    console.show_activity()
    downloaded_file = yt.streams \
        .filter(progressive=True, file_extension='mp4') \
        .order_by('resolution') \
        .desc() \
        .first() \
        .download(output_path=outdir)
    print("Downloaded to", downloaded_file)
    console.hide_activity()
    return downloaded_file


console.clear()

mp4_files: str = Path("tubes.txt").read_text()
tubes = set(mp4_files.splitlines())
downloaded_tubes = set()
for vid in tubes:
    if not vid:
        continue

    download_video(vid)
    downloaded_tubes.add(vid)
    output_list = f"{os.linesep}".join(tubes - downloaded_tubes)
    Path("tubes.txt").write_text(output_list)

print(f"✅ Finished. Downloaded {len(tubes)} videos")
