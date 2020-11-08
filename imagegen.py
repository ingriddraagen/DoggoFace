from __future__ import print_function
import os
import random
import time
from PIL import Image, ImageDraw, ImageEnhance, ImageChops
from floodfill import aggressive_floodfill
import time


BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))) + r"/DoggoFace/Doggoparts/"


# Folder-location of components:
face_base_folder = BASE_DIR + r"Face/"
face_feature_folder = BASE_DIR + r"Face_Features/"
texture_folder = BASE_DIR + r"Textures/"
accessories_folder = BASE_DIR + r'Accessories/'


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

    # To generate only one image:
    make_face()

    # For a continuous face-generation:
    # make_face_continuous()

    # To generate several faces:
    # make_face_continuous(<filename>)


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

    hat_probability = 0
    is_season = False

    face_shape = Image.new('RGBA', (width, height), color=(255, 255, 255, 0))
    face_base = Image.new('RGBA', (width, height), color=(255, 255, 255, 0))
    face = Image.new('RGBA', (width, height), color=(255, 255, 255, 0))
    texture = Image.new('RGBA', (width, height), color=(255, 255, 255, 255))
    background_mask = Image.new(
        'RGBA', (width, height), color=(255, 255, 255, 0))
    face_mask = Image.new('RGBA', (width, height), color=(255, 255, 255, 0))
    background = Image.new('RGBA', (width, height),
                           color=random.choice(background_colors))
    hat_file = random_file_from_dir(accessories_folder + 'Hats/')
    # Selecting texture
    insert_random_imagelayer_to_image(texture_folder, texture)

    hat = random.randint(1, 100)

    if hat < hat_probability:
        hat = True

    # Selecting the face-shape and ears
    for folder in os.listdir(face_base_folder):
        folder = folder + '/'
        if 'Faceshapes' in folder:
            faceshape = random_file_from_dir(face_base_folder + folder)
            insert_layer_to_image(faceshape, face_shape)
            insert_layer_to_image(faceshape, face_base)
            continue
        elif (hat and no_ear(hat_file)):
            if 'Ears' in folder:
                continue
        imagelocation = face_base_folder + folder
        insert_random_imagelayer_to_image(imagelocation, face_base)

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
    face.paste(background, (0, 0), background)

    # Adding faceparts to the face

    # Eyes
    folder = "00_Eyes_mask/"
    use_mask_filename = random_file_from_dir(face_feature_folder + folder)
    use_mask = open_image_file(use_mask_filename)
    if (mask(use_mask_filename)):
        use_mask = ImageChops.multiply(face_mask, use_mask)
        face.paste(use_mask, (0, 0), use_mask)

    # Mouth
    folder = "01_Mouth_fill/"
    file_to_fill = random_file_from_dir(face_feature_folder + folder)
    insert_layer_to_image(file_to_fill, face)
    if fill(file_to_fill):
        face = face.convert('RGB')
        aggressive_floodfill(face, xy=(width*0.5, height*0.7),
                             value=get_corner_color(texture))

    # Nose
    folder = "02_Noses/"
    imagelocation = face_feature_folder + folder
    insert_random_imagelayer_to_image(imagelocation, face)

    if (hat < hat_probability):
        for folder in os.listdir(accessories_folder):
            if 'Seasonal' in folder and not is_season:
                continue
            folder = folder + '/'
            imagelocation = accessories_folder + folder
            insert_random_imagelayer_to_image(imagelocation, face)

    return face


if __name__ == '__main__':
    main()
