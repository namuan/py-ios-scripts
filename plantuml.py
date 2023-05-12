import base64
import string
import webbrowser
import zlib

import appex
import clipboard

maketrans = bytes.maketrans

plantuml_alphabet = string.digits + string.ascii_uppercase + string.ascii_lowercase + '-_'
base64_alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
b64_to_plantuml = maketrans(base64_alphabet.encode('utf-8'), plantuml_alphabet.encode('utf-8'))


def deflate_and_encode(plantuml_text):
    zlibbed_str = zlib.compress(plantuml_text.encode('utf-8'))
    compressed_string = zlibbed_str[2:-4]
    return base64.b64encode(compressed_string).translate(b64_to_plantuml).decode('utf-8')


def generate_plantuml_url():
    if appex.get_text():
        plantuml_text = appex.get_text()
    elif clipboard.get():
        plantuml_text = clipboard.get()
    else:
        return None

    encoded_text = deflate_and_encode(plantuml_text)

    return 'http://www.plantuml.com/plantuml/img/' + encoded_text


url = generate_plantuml_url()
if url:
    print(url)
    webbrowser.open(url)
else:
    print('This script can only be used with PlantUML Text')
