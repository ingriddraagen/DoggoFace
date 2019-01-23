from __future__ import print_function
import os
import random
from PIL import Image, ImageDraw

# Generate background image, choose from a selection of bg_colors (pretty pink, beautiful blue, etc.)
bg_colors = [
    (252, 156, 246),  # pink
    (102, 153, 255),  # blue
]

# rgba color
dog_colors = [
    (170, 170, 170, 255),  # grey
    (139, 69, 19, 255),  # brown
]
background = Image.new('RGB', (2048, 2048), color=random.choice(bg_colors))

for folder in os.listdir('Doggoparts/'):
    img_folder = 'Doggoparts/' + folder + '/'
    img = Image.open(
        img_folder + random.choice(os.listdir(img_folder))
    )

    if folder == '02_Faceshapes':
        width, height = img.size
        center = (int(0.5 * width), int(0.5 * height))
        yellow = (255, 255, 0, 255)
        ImageDraw.floodfill(img,  xy=center, value=random.choice(dog_colors))

    background.paste(img, (0, 0), img)

background.save('image.png')
