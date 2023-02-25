#!python3

from __future__ import unicode_literals
import appex
import console
import clipboard
import os
import sys
from pytube import YouTube

outdir = os.path.expanduser("~/Documents/Downloads")
try:
    os.mkdir(outdir)
except FileExistsError:
    pass

url = None
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

yt = YouTube(url)
print("Starting download of", yt.title)
downloaded_file = yt.streams\
    .filter(progressive=True, file_extension='mp4')\
    .order_by('resolution')\
    .desc()\
    .first()\
    .download(output_path=outdir)
print("Downloaded to", downloaded_file)
# console.open_in(downloaded_file)
