from __future__ import print_function
import os
import random
from PIL import Image, ImageDraw
from floodfill import aggressive_floodfill


# Generate background image, choose from a selection of bg_colors (pretty pink, beautiful blue, etc.)
bg_colors = [
    (252, 156, 246, 255),  # pink
    (102, 153, 255, 255),  # blue
    (233, 175, 163),
    (238, 66, 102),
    (255, 210, 63),
    (84, 13, 110),
    (243, 252, 240),
    (255, 200, 87),
    (233, 114, 76),
]
# Selecting a random texture for the dog-s fur
texture_choice = Image.open("Doggoparts/00_Texture/" + random.choice(os.listdir("Doggoparts/00_Texture/")))

# Ingrid fucker opp alt

def insert_layer_to_image(image, layer):
    image.paste(layer, (0, 0), layer)
    return

def return_radom_file_from_dir(dir):
    return (random.choice(os.listdir(dir)))

def open_random_image_file(dir, random):
    return (Image.open(dir + random))

def make_base():
    base = Image.new('RGB', (2048, 2048), color=(0, 255, 255))
    ear =  Image.open("Doggoparts/01_Ears/" + random.choice(os.listdir("Doggoparts/01_Ears/")))
    face =  Image.open("Doggoparts/02_Faceshapes/" + random.choice(os.listdir("Doggoparts/02_Faceshapes/")))
    eyes =  Image.open("Doggoparts/03_Eyes/" + random.choice(os.listdir("Doggoparts/03_Eyes/")))
    insert_layer_to_image(base, texture_choice)
    insert_layer_to_image(base, ear)
    insert_layer_to_image(base, eyes)
    insert_layer_to_image(base, face)
    base.save('Outputs/base.png')

def fill(layer):
    if( layer[0] == 'n'):
        return False
    return True

def get_mouth_color(base):
    rgb_im = base.convert('RGB')
    mouth_color = rgb_im.getpixel((0, 0))
    return mouth_color



def finish_base():
    doggoface = Image.open('Outputs/base.png')
    accessory_filename = random.choice(os.listdir("Doggoparts/04_Accessories/"))
    accessory =  Image.open("Doggoparts/04_Accessories/" + accessory_filename)
    insert_layer_to_image(doggoface, accessory)
    if fill(accessory_filename):
        ImageDraw.floodfill(doggoface, xy=(1000, 1200), value=mouth_color, thresh=10)
    nose =  Image.open("Doggoparts/05_Noses/" + random.choice(os.listdir("Doggoparts/05_Noses/")))
    insert_layer_to_image(doggoface, nose)
    aggressive_floodfill(doggoface,  xy=(0, 0), value=random.choice(bg_colors))

    doggoface.save('Outputs/doggo.png')

make_base()

finish_base()



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
