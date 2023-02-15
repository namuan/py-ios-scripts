#!python3

from __future__ import unicode_literals
import yt_dlp as youtube_dl
import appex
import console
import clipboard
import os
import sys
from pathlib import Path
import shutil

outdir = os.path.expanduser("~/Documents/Downloads")
try:
	os.mkdir(outdir)
except FileExistsError:
	pass

ydl_opts = {
	'outtmpl': os.path.join(outdir, '%(title)s.%(ext)s'),
	"socket_timeout": 10,
	"retries": 10,
	"noplaylist": True,
	"quiet": True,
	"no_warnings": True,
}

def download_video(url):
	print("URL: ", url)
	
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		console.show_activity()
		info = ydl.extract_info(url, download=True)
		filepath = ydl.prepare_filename(info)
		print(f"File downloaded {filepath}")
		console.hide_activity()

console.clear()

mp4_files: str = Path("tubes.txt").read_text()
tubes = set(mp4_files.splitlines())
downloaded_tubes = set()
for vid in tubes:
	if not vid:
		continue
		
	console.show_activity()
	print(f"🏎 Processing {vid}")
	download_video(vid)
	downloaded_tubes.add(vid)
	output_list = f"{os.linesep}".join(tubes - downloaded_tubes)
	Path("tubes.txt").write_text(output_list)
	console.hide_activity()
	
print(f"✅ Finished. Downloaded {len(tubes)} videos")
