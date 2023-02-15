#!python3

from __future__ import unicode_literals
import yt_dlp as youtube_dl
import appex
import console
import clipboard
import os
import sys

outdir = os.path.expanduser("~/Documents/Downloads")
try:
	os.mkdir(outdir)
except FileExistsError:
	pass
	
if appex.get_attachments():
	# e.g. share from YouTube app
	url = appex.get_attachments()[0]
elif appex.get_urls():
	# e.g. share from Safari
	url = appex.get_urls()[0]
elif appex.get_text():
	url = appex.get_text()
elif clipboard.get():
	url = clipboard.get()
	
print("URL: ", url)
if not url or not url.startswith("http"):
	url = input("No URL found - enter URL to download: ")
	
ydl_opts = {
	'outtmpl': os.path.join(outdir, '%(title)s.%(ext)s'),
	"socket_timeout": 10,
	"retries": 10,
	"noplaylist": True,
	"quiet": True,
	"no_warnings": True,
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	info = ydl.extract_info(url, download=True)
	filepath = ydl.prepare_filename(info)

console.open_in(filepath)
