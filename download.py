import os
import urllib.request
import zipfile
import shutil

main_dir = 'py-ios-scripts-main'

if os.path.exists(main_dir):
    os.system(f'rm -rf {main_dir}')

url = 'https://github.com/namuan/py-ios-scripts/archive/refs/heads/main.zip'
urllib.request.urlretrieve(url, 'main.zip')

with zipfile.ZipFile('main.zip', 'r') as zip_ref:
    zip_ref.extractall()

os.remove('main.zip')

shutil.copy(os.path.join(main_dir, 'download.py'), '.')

print("Done")
