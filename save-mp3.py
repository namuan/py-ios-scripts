#!python3

from __future__ import unicode_literals

import os

import appex
import clipboard
import console
from pytube import YouTube

outdir = os.path.expanduser("~/Documents/Downloads/mp3")
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


def download_audio(url):
    yt = YouTube(url)
    print("Starting download of", yt.title)
    console.show_activity()
    downloaded_file = yt.streams \
        .filter(only_audio=True, mime_type="audio/mp4") \
        .order_by('abr') \
        .desc() \
        .first() \
        .download(output_path=outdir)
    print("Downloaded to", downloaded_file)
    console.hide_activity()
    return downloaded_file


downloaded_file = download_audio(url)
console.open_in(downloaded_file)
