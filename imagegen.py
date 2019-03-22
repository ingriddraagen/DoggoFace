import os
import random
from PIL import Image, ImageChops
from .floodfill import aggressive_floodfill  # slight modification of PIL's floodfill function

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r"/DoggoFace/Doggoparts/"
# Folder-location of components:
face_base_folder = BASE_DIR + "Face/"
face_features_folder = BASE_DIR + "Face_Features/"
texture_folder = BASE_DIR + "Textures/"
background_color_folder = BASE_DIR + "Background_Colors/"


def paste_layer_onto_image(layer, image):
    layer = Image.open(layer)
    image.paste(layer, (0, 0), layer)


def random_file_from_dir(directory):
    return directory + random.choice(os.listdir(directory))


def paste_random_layer_onto_image(folder_name, image):
    paste_layer_onto_image(random_file_from_dir(folder_name), image)


def get_corner_color(image):
    return image.getpixel((0, 0))


def generate_face():
    width, height = Image.open(random_file_from_dir(texture_folder)).size  # image should be square
    face_shape = Image.new('RGBA', (width, height), color=(255, 255, 255, 0))
    face_base = Image.new('RGBA', (width, height), color=(255, 255, 255, 0))
    texture = Image.new('RGBA', (width, height), color=(255, 255, 255, 255))
    background_mask = Image.new('RGBA', (width, height), color=(255, 255, 255, 0))
    face_mask = Image.new('RGBA', (width, height), color=(255, 255, 255, 0))

    # Selecting texture
    paste_random_layer_onto_image(texture_folder, texture)

    # Selecting the face-shape and ears
    for folder_name in sorted(os.listdir(face_base_folder)):
        layer = random_file_from_dir(face_base_folder + folder_name + '/')
        if 'Faceshapes' in folder_name:
            paste_layer_onto_image(layer, face_shape)
            paste_layer_onto_image(layer, face_base)
        else:
            paste_layer_onto_image(layer, face_base)

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

    # Combining the face_shape, texture and background color
    face = ImageChops.multiply(face_base, texture)
    background = ImageChops.multiply(Image.open(random_file_from_dir(background_color_folder)), background_mask)
    face.paste(background, (0, 0), background)

    # Adding faceparts to the face
    for folder_name in sorted(os.listdir(face_features_folder)):
        layer = random_file_from_dir(face_features_folder + folder_name + '/')
        if 'fill' not in folder_name and 'mask' not in folder_name:
            paste_layer_onto_image(layer, face)
        elif 'fill' in folder_name:
            paste_layer_onto_image(layer, face)
            if 'no_fill' not in layer:
                face = face.convert('RGB')
                aggressive_floodfill(face, xy=(width*0.5, height*0.7), value=get_corner_color(texture))
        else:
            use_mask = Image.open(layer)
            if 'mask' in layer:
                use_mask = ImageChops.multiply(face_mask, use_mask)
            face.paste(use_mask, (0, 0), use_mask)

    return face
