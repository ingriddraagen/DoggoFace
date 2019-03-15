import os
import random
from PIL import Image
from .floodfill import aggressive_floodfill

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r"/DoggoFace/Doggoparts/"

# Folder-location of components:
face_parts_folder = BASE_DIR + r"Face_Features/"
texture_folder = BASE_DIR + r"Textures/"
background_color_folder = BASE_DIR + r"Background_Colors/"


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
    width, height = Image.open(random_file_from_dir(texture_folder)).size
    image_size = width
    face = Image.new('RGB', (image_size, image_size), color=(0, 255, 255))
    # Adding random texture (the doggos fur) to the image
    paste_random_layer_onto_image(texture_folder, face)

    # stack doogo-layers onto the image
    for folder_name in sorted(os.listdir(face_parts_folder)):  # bugs out on linux of not sorted
        folder_name += '/'
        layer = random_file_from_dir(face_parts_folder + folder_name)
        paste_layer_onto_image(layer=layer, image=face)
        if 'fill' in folder_name and 'no_fill' not in layer:
            aggressive_floodfill(face, xy=(image_size * 0.5, image_size * 0.7), value=get_corner_color(face))
    # Filling in the background color:
    aggressive_floodfill(face, xy=(0, 0),
                         value=get_corner_color(Image.open(random_file_from_dir(background_color_folder))))
    return face
