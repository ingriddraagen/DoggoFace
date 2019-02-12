from __future__ import print_function
import os
import random
from PIL import Image, ImageDraw
from floodfill import aggressive_floodfill

# TODO: Gjør bakgrunn til alle hundedeler gjennomsiktig, også på innsiden.
#  Modifiser floodfill() til å kun stoppe ved svarte streker

# Generate background image, choose from a selection of bg_colors (pretty pink, beautiful blue, etc.)
bg_colors = [
    (252, 156, 246, 255),  # pink
    (102, 153, 255, 255),  # blue
]
background = Image.new('RGB', (2048, 2048), color=(0, 255, 255))

for folder in os.listdir('Doggoparts/'):
    img_folder = 'Doggoparts/' + folder + '/'
    img = Image.open(
        img_folder + random.choice(os.listdir(img_folder))
    )
    background.paste(img, (0, 0), img)

aggressive_floodfill(background,  xy=(0, 0), value=random.choice(bg_colors))
background.save('image.png')
