from __future__ import print_function
import os
import random
from PIL import Image

# Generate background image, choose from a selection of colors (pretty pink, beautiful blue, etc.)
colors = [
    (252, 156, 246),  # pink
    (102, 153, 255),  # blue
]
background = Image.new('RGB', (2048, 2048), color=random.choice(colors))

for folder in os.listdir('Doggoparts/'):
    img_folder = 'Doggoparts/' + folder + '/'
    img = Image.open(
        img_folder + random.choice(os.listdir(img_folder))
    )
    background.paste(img, (0, 0), img)

background.save('image.png')
