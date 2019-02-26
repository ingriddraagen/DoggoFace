from __future__ import print_function
import os
import random
import time
from PIL import Image, ImageDraw
from floodfill import aggressive_floodfill


image_size = 0
width = 0

face_parts_folder = "Doggoparts/facecomponents/"
texture_folder = "Doggoparts/00_Texture/"

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

def main():

    # Determining the size of the inputimages
    width, height = open_image_file(random_file_from_dir(texture_folder)).size
    image_size = width
    print (image_size)



    while True:
        start = time.time()
        make_face(face_parts_folder)
        end = time.time()
        print(end - start)
        print(" ")


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

def make_face(face_parts_folder):
    width, height = open_image_file(random_file_from_dir(texture_folder)).size
    image_size = width
    print (image_size)
    face =  Image.new('RGB', (image_size, image_size), color=(0, 255, 255))
    # Adding random texture to the image
    insert_random_imagelayer_to_image('Doggoparts/00_Texture/', face)

    # Adding faceparts to the image, in the
    for folder in os.listdir(face_parts_folder):
        folder = folder + '/'
        if ('fill' not in folder and 'ignore' not in folder):
            imagelocation = face_parts_folder + folder
            insert_random_imagelayer_to_image( imagelocation, face )
        else:
            if 'ignore' in folder:
                continue
            elif 'fill' in folder:
                file_to_fill = random_file_from_dir(face_parts_folder + folder)
                insert_layer_to_image( file_to_fill , face )
                if fill(file_to_fill):
                    print('filling')
                    print(face)
                    aggressive_floodfill(face, xy=(image_size*0.5, image_size*0.7), value=get_corner_color(face))
    aggressive_floodfill(face,  xy=(0, 0), value=random.choice(bg_colors)) # Filling in the background color
    face.save('Outputs/face.png')



if __name__ == '__main__':
    main()
