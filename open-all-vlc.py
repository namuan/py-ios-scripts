# open all mp4 files in console share window
# and delete after shared successfully
from pathlib import Path
import console 
import photos
import os

mp4_files = Path("Downloads").glob("*.mp4")
for f in mp4_files:
	filepath = f.as_posix()
	#console.quicklook(filepath)
	console.open_in(filepath)
	print(f"Removing {filepath}")
	os.remove(filepath)
