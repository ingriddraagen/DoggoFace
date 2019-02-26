from __future__ import print_function
import os
import random
import time
from PIL import Image, ImageDraw
from floodfill import aggressive_floodfill

# Initiating variables:
image_size = 0
width = 0
iterations = 0

# Folder-location of components:
outer_folder = "Doggoparts/"
face_parts_folder = outer_folder + "Face_Features/"
texture_folder = outer_folder + "Textures/"
background_color_folder = outer_folder + "Background_Colors/"

# Where the finished image should be saved.
output_file = "Outputs/face.png"
    # Should you wish to make lots of faces:
'''
output_file = "Outputs/face" + iterations + ".png"
'''


# This is where the magic happens:
def main():
    # Determining the size of finished image:
    width, height = open_image_file(random_file_from_dir(texture_folder)).size
    image_size = width

    # Printing how many possible combinations there are, cuz its fun:
    print ("There are " + int_presentation(how_many_combinations_are_there()) + " possible compinations")
    print (" ")
    print ("Now let's make some doggos!")
    print (" ")

    while True:
        start = time.time()
        make_face(face_parts_folder)
        end = time.time()
        print("time to complete image: " + str(end - start))
        print(" ")

def int_presentation(int):
    i = -3
    j = None
    original_int = int
    int_string = ""
    while -i <= len(str(int))+3:
        sub_string = str(original_int)[i:j]
        if (len(sub_string) == 3):
            sub_string = " " + sub_string
        int_string = sub_string + int_string
        j = i
        i -= 3
    return (int_string)

def how_many_combinations_are_there():
    possible_combinations = 0
    files = 0
    # number of textures:
    for file in os.listdir(texture_folder):
        possible_combinations += 1

    # number of background colors:
    for file in os.listdir(background_color_folder):
        files += 1
    possible_combinations = possible_combinations * files
    files = 0

    # number of different face-shapes
    for folder in os.listdir(face_parts_folder):
        folder = folder + "/"
        for file in os.listdir(face_parts_folder+folder):
            files += 1
        possible_combinations = possible_combinations * files
        files = 0
    return (possible_combinations)

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
    global iterations
    width, height = open_image_file(random_file_from_dir(texture_folder)).size
    image_size = width
    face =  Image.new('RGB', (image_size, image_size), color=(0, 255, 255))
    # Adding random texture to the image
    insert_random_imagelayer_to_image(texture_folder, face)

    # Adding faceparts to the image, in the
    for folder in os.listdir(face_parts_folder):
        folder = folder + '/'
        if ('fill' not in folder):
            imagelocation = face_parts_folder + folder
            insert_random_imagelayer_to_image( imagelocation, face )
        else:
            file_to_fill = random_file_from_dir(face_parts_folder + folder)
            insert_layer_to_image( file_to_fill , face )
            if fill(file_to_fill):
                aggressive_floodfill(face, xy=(image_size*0.5, image_size*0.7), value=get_corner_color(face))
    # Filling in the background color:
    aggressive_floodfill(face,  xy=(0, 0), value=get_corner_color(open_image_file(random_file_from_dir(background_color_folder))))
    face.save(output_file)
    iterations += 1



if __name__ == '__main__':
    main()
