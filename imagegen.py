from __future__ import print_function
import os
import random
from PIL import Image, ImageDraw
from floodfill import aggressive_floodfill


# Background colors
bg_colors = [
    (252, 156, 246),  # pink
    (102, 153, 255),  # blue
    (233, 175, 163),
    (238, 66, 102),
    (255, 210, 63),
    (84, 13, 110),
    (243, 252, 240),
    (255, 200, 87),
    (233, 114, 76),
]

def insert_layer_to_image(imagefile, image):
    layer = open_image_file(imagefile)
    image.paste(layer, (0, 0), layer)
    return

def random_file_from_dir(dir):
    return (dir + random.choice(os.listdir(dir)))

def open_image_file(imagefile):
    return (Image.open(imagefile))

def insert_random_imagelayer_to_image(dir, image):
    insert_layer_to_image(random_file_from_dir(dir), image)

def fill(layer):
    if('no_fill' in layer):
        return False
    return True

def get_corner_color(image):
    return (image.getpixel((0, 0)))

def make_base_from_x_first_folders(face_parts_folder, x):
    base =  Image.new('RGB', (2048, 2048), color=(0, 255, 255))
    for folder in os.listdir('Doggoparts/')[:x]:
        folder = folder + '/'
        imagelocation = face_parts_folder + folder
        insert_random_imagelayer_to_image( imagelocation, base)
    base.save('Outputs/base.png')

def finish_base(face_parts_folder, x):
    face = Image.open('Outputs/base.png')

    for folder in os.listdir('Doggoparts/')[x:]:
        folder = folder + '/'
        if ('fill' not in folder and 'ignore' not in folder):
            imagelocation = face_parts_folder + folder
            insert_random_imagelayer_to_image( imagelocation, face)
        else:
            if 'ignore' in folder:
                continue
            elif 'fill' in folder:
                file_to_fill = random_file_from_dir(face_parts_folder + folder)
                print (file_to_fill)
                insert_layer_to_image( file_to_fill , face )
                if fill(file_to_fill):
                    ImageDraw.floodfill(face, xy=(1000, 1200), value=get_corner_color(face), thresh=10)
    aggressive_floodfill(face,  xy=(0, 0), value=random.choice(bg_colors)) # Filling in the background color
    face.save('Outputs/face.png')

def make_face( face_parts_folder, x ):
    make_base_from_x_first_folders( face_parts_folder, x )
    finish_base( face_parts_folder, x)

while True:
    make_face("Doggoparts/", 3)
