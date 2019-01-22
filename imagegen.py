# Combine multiple images into one.
#
# To install the Pillow module on Mac OS X:
#
# $ xcode-select --install
# $ brew install libtiff libjpeg webp little-cms2
# $ pip install Pillow
#

from __future__ import print_function
import os

from PIL import Image

os.listdir()
files = [
'Ears/1.png',
'Faceshapes/1.png',
  'Eyes/1.png',
  'Accessories/1.png',
  'Noses/1.png']



background = Image.open(files[0])

for file in files[1:]:
    img = Image.open(file)
    background.paste(img,(0, 0), img)

background.show()
