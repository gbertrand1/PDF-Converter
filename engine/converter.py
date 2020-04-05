import sys
import os
from pdf2image import convert_from_path

path = os.path.abspath(sys.argv[1])
filename = os.path.split(path)[1]
filepath = os.path.split(path)[0]
name = filename.split('.')[0]

pages = convert_from_path(path, 720)

if len(pages) == 1:
    for page in pages:
        jpgname = "{}.jpg".format(name)
        page.save(os.path.join(filepath, jpgname), 'JPEG')
else:
    for idx, page in pages:
        jpgname = "{}-{}.jpg".format(name, idx)
        page.save(os.path.join(filepath, jpgname), 'JPEG')

