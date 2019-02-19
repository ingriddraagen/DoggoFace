from __future__ import print_function
import os
import random
from PIL import Image, ImageDraw
from floodfill import aggressive_floodfill


# Generate background image, choose from a selection of bg_colors (pretty pink, beautiful blue, etc.)
bg_colors = [
    (252, 156, 246, 255),  # pink
    (102, 153, 255, 255),  # blue
]
background = Image.new('RGB', (2048, 2048), color=(0, 255, 255))

# Ingrid fucker opp alt

base = Image.new('RGB', (2048, 2048), color=(0, 255, 255))
ear =  Image.open("Doggoparts/04_Ears/" + random.choice(os.listdir("Doggoparts/04_Ears/")))
face =  Image.open("Doggoparts/01_Faceshapes/" + random.choice(os.listdir("Doggoparts/01_Faceshapes/")))
eyes =  Image.open("Doggoparts/03_Eyes/" + random.choice(os.listdir("Doggoparts/03_Eyes/")))
texture_choice = Image.open("Doggoparts/00_Texture/" + random.choice(os.listdir("Doggoparts/00_Texture/")))


base.paste(texture_choice, (0, 0), texture_choice)
base.paste(ear, (0, 0), ear)
base.paste(eyes, (0, 0), eyes)
base.paste(face, (0, 0), face)
base.save('base.png')

snoot = Image.open('base.png')
snooty =  Image.open("Doggoparts/02_Accessories/" + random.choice(os.listdir("Doggoparts/02_Accessories/")))
rgb_im = base.convert('RGB')
mouth_color = rgb_im.getpixel((0, 0))
snoot.paste(snooty, (0, 0), snooty)
ImageDraw.floodfill(snoot, xy=(1000, 1200), value=mouth_color, thresh=10)

nose =  Image.open("Doggoparts/05_Noses/" + random.choice(os.listdir("Doggoparts/05_Noses/")))
snoot.paste(nose, (0, 0), nose)
aggressive_floodfill(snoot,  xy=(0, 0), value=random.choice(bg_colors))

snoot.save('snootes.png')


'''
base.paste(snoot)
base.show()
base.save('testing.png')
'''

#base = Image.new('RGB', (2048, 2048), color=(0, 255, 255))
#background.paste(texture_choice, (0, 0), texture_choice)
#
#
#mouth =  Image.open("Doggoparts/02_Accessories/" + random.choice(os.listdir("Doggoparts/02_Accessories/")))
#rgb_im = background.convert('RGB')
#mouth_color = rgb_im.getpixel((0, 0))
#mouth.save("temp.png")
#aggressive_floodfill(mouth, xy=(900, 1400), value=mouth_color)
#background.paste(mouth, (0, 0), mouth)
#
#
#
#
#mouthfilled = Image.new('RGB', (2048, 2048), color=(0, 255, 255))
#mouth =  Image.open("Doggoparts/02_Accessories/" + random.choice(os.listdir("Doggoparts/02_Accessories/")))
#mouth_color = rgb_im.getpixel((0, 0))
#aggressive_floodfill(mouth, xy=(900, 1400), value=mouth_color)
#background.paste(mouth, (0, 0), mouth)
#
## med mindre dette faktisk funker
#
#
#for folder in os.listdir('Doggoparts/')[1:]:
#
#    img_folder = 'Doggoparts/' + folder + '/'
#    if img_folder == "Doggoparts/02_Accessories/":
#        mouth =  Image.open("Doggoparts/02_Accessories/" + random.choice(os.listdir("Doggoparts/02_Accessories/")))
#        rgb_im = background.convert('RGB')
#        mouth_color = rgb_im.getpixel((0, 0))
#        mouth.save("temp.png")
#        aggressive_floodfill(mouth, xy=(900, 1400), value=mouth_color)
#        background.paste(mouth, (0, 0), mouth)
#        continue
#    img = Image.open(
#        img_folder + random.choice(os.listdir(img_folder))
#    )
#    print(img_folder)
#    background.paste(img, (0, 0), img)
#
#
#aggressive_floodfill(background,  xy=(0, 0), value=random.choice(bg_colors))
#background.save('image.png')
#
