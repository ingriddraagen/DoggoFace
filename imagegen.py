from __future__ import print_function
import os
import random
import time
from PIL import Image, ImageDraw, ImageEnhance, ImageChops
from floodfill import aggressive_floodfill
import time

# Initiating variables:
iterations = 0

# Folder-location of components:
outer_folder = "Doggoparts/"
face_base_folder = outer_folder + "Face/"
face_feature_folder = outer_folder + "Face_Features/"
texture_folder = outer_folder + "Textures/"
accessories_folder = outer_folder + 'Accessories/'

# Where the finished image should be saved.
output_folder = "Outputs/"
output_file_name = output_folder + "face.png"


background_colors = [(32, 30, 80, 255),
    (252, 122, 87, 255),
    (99, 193, 50, 255),
    (53, 134, 0, 255),
    (233, 210, 244, 255),
    (99, 176, 205, 255),
    (27, 153, 139, 255),
    (150, 224, 114, 255),
    (252, 175, 88, 255),
    (247, 92, 3, 255),
    (4, 167, 119, 255),
    (255, 135, 57, 255),
    (229, 116, 188, 255),
    (34, 116, 165, 255),
    (221, 44, 100, 255),
    (193, 121, 185, 255),
    (255, 67, 101, 255),
    (245, 83, 154, 255),
    (153, 0, 255, 255),
    (45, 93, 123, 255),
    (130, 2, 99, 255),
    (252, 211, 45, 255),
    (221, 44, 100, 255),
    (196, 241, 190, 255),
    (159, 216, 203, 255)]

# This is where the magic happens:
def main():
    # Determining the size of finished image:
    width, height = open_image_file(random_file_from_dir(texture_folder)).size
    make_face_continuous()

    # To generate only one image:
    # make_face()

    # For a continuous face-generation:
    # make_face_continuous()

    # To generate several faces:
    # make_face_continuous(<filename>)



def make_face_continuous(file_name = output_file_name):
    # Printing how many possible combinations there are, cuz its fun:
    print ("There are " + int_presentation(how_many_combinations_are_there()) + " possible combinations")
    print (" ")
    print ("Now let's make some doggos!")
    print (" ")
    global iterations
    global output_file_name
    if (output_file_name is not file_name):
        while True:
            output_file_name = output_folder + file_name + str(iterations) + ".png"
            start = time.time()
            make_face()
            iterations += 1
            end = time.time()
            print("time to complete image: " + str(end - start))
            print(" ")
            time.sleep(5)


    else:
        while True:
            start = time.time()
            make_face()
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
    possible_combinations = 1
    files = 0
    # number of textures:
    for category_folder in os.listdir(outer_folder):
        category_folder = outer_folder + category_folder + '/'
        for folder in os.listdir(category_folder):
            folder = category_folder + folder + '/'
            if 'Texture' in folder or 'Seasonal' in folder:
                continue
            for file in os.listdir(folder):
                files += 1
            possible_combinations = files *possible_combinations
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
    return 'no_fill' not in layer

def mask(layer):
    return 'mask' in layer

def no_ear(layer):
    return 'no_ear' in layer

def get_corner_color(image):
    return (image.getpixel((0, 0)))


def make_face():
    width, height = open_image_file(random_file_from_dir(texture_folder)).size

    hat_probability = 100
    is_season = False

    face_shape = Image.new('RGBA', (width, height), color = (255, 255, 255, 0) )
    face_base =  Image.new('RGBA', (width, height), color = (255, 255, 255, 0) )
    face =  Image.new('RGBA', (width, height), color = (255, 255, 255, 0) )
    texture = Image.new('RGBA', (width, height), color = (255, 255, 255, 255) )
    background_mask = Image.new('RGBA', (width, height), color = (255, 255, 255, 0))
    face_mask = Image.new('RGBA', (width, height), color = (255, 255, 255, 0))
    background = Image.new('RGBA', (width, height), color = random.choice(background_colors))
    # Selecting texture
    insert_random_imagelayer_to_image(texture_folder, texture)

    hat = random.randint(1,100)

    if hat < hat_probability:
        hat = True
        hat_file = random_file_from_dir(accessories_folder + 'Hats/')

    # Selecting the face-shape and ears
    for folder in os.listdir(face_base_folder):
        folder = folder + '/'
        if 'Faceshapes' in folder:
            faceshape = random_file_from_dir(face_base_folder + folder)
            insert_layer_to_image( faceshape , face_shape )
            insert_layer_to_image( faceshape , face_base )
            continue
        elif ( hat and no_ear(hat_file) ):
            print (( hat and no_ear(hat_file)))
            if 'Ears' in folder:
                continue
        imagelocation = face_base_folder + folder
        insert_random_imagelayer_to_image( imagelocation, face_base )

    # Creating a mask for the background
    face_base_data = face_base.getdata()
    background_data = []
    for pixel in face_base_data:
        if pixel[3] > 100:
            background_data.append((255, 255, 255, 0))
        else:
            background_data.append((255, 255, 255, 255))
    background_mask.putdata(background_data)


    # Creating a mask for the face
    face_shape_data = face_shape.getdata()
    face_data = []
    for pixel in face_shape_data:
        if pixel[3] < 10:
            face_data.append((255, 255, 255, 0))
        else:
            face_data.append((255, 255, 255, 255))
    face_mask.putdata(face_data)

    # Combining the faceshape, texture and background color
    face = ImageChops.multiply(face_base, texture)
    background = ImageChops.multiply(background, background_mask)
    face.paste(background, (0,0), background)


    # Adding faceparts to the face
    for folder in os.listdir(face_feature_folder):
        folder = folder + '/'
        if ('fill' not in folder and 'mask' not in folder):
            imagelocation = face_feature_folder + folder
            insert_random_imagelayer_to_image( imagelocation, face )
        elif ('fill' in folder):
            file_to_fill = random_file_from_dir(face_feature_folder + folder)
            insert_layer_to_image( file_to_fill , face )
            if fill(file_to_fill):
                print ('filling')
                face = face.convert('RGB')
                aggressive_floodfill(face, xy=(width*0.5, height*0.7), value=get_corner_color(texture))
        else:
            use_mask_filename = random_file_from_dir(face_feature_folder + folder)
            use_mask = open_image_file(use_mask_filename)
            if (mask(use_mask_filename)):
                use_mask = ImageChops.multiply(face_mask, use_mask)
            face.paste(use_mask, (0,0), use_mask)
    random_number = random.randint(1,101)

    if (hat < hat_probability):
        for folder in os.listdir(accessories_folder):
            if 'Seasonal' in folder and not is_season:
                continue
            folder = folder + '/'
            imagelocation = accessories_folder + folder
            insert_random_imagelayer_to_image( imagelocation, face )


    face.save(output_file_name)



if __name__ == '__main__':
    main()
