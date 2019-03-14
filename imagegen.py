import os
import random
from PIL import Image
from .floodfill import aggressive_floodfill

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Folder-location of components:
outer_folder = BASE_DIR + r"/DoggoFace/Doggoparts/"
face_parts_folder = outer_folder + r"Face_Features/"
texture_folder = outer_folder + r"Textures/"
background_color_folder = outer_folder + r"Background_Colors/"

# Where the finished image should be saved.
output_folder = BASE_DIR + r"/DoggoFace/Outputs/"
output_file_name = output_folder + "face.png"


def generate_face():
    make_face()


def insert_layer_to_image(layer, image):
    layer = Image.open(layer)
    image.paste(layer, (0, 0), layer)


def random_file_from_dir(directory):
    return directory + random.choice(os.listdir(directory))


def insert_random_imagelayer_to_image(dir, image):
    insert_layer_to_image(random_file_from_dir(dir), image)


def fill(layer):
    return 'no_fill' in layer


def get_corner_color(image):
    return image.getpixel((0, 0))


def make_face():
    width, height = Image.open(random_file_from_dir(texture_folder)).size
    image_size = width
    face = Image.new('RGB', (image_size, image_size), color=(0, 255, 255))
    # Adding random texture to the image
    insert_random_imagelayer_to_image(texture_folder, face)

    # Adding faceparts to the image, in the
    for folder in os.listdir(face_parts_folder):
        folder = folder + '/'
        if 'fill' not in folder:
            image_location = face_parts_folder + folder
            insert_random_imagelayer_to_image(image_location, face)
        else:
            file_to_fill = random_file_from_dir(face_parts_folder + folder)
            insert_layer_to_image(file_to_fill, face)
            if fill(file_to_fill):
                aggressive_floodfill(face, xy=(image_size * 0.5, image_size * 0.7), value=get_corner_color(face))
    # Filling in the background color:
    aggressive_floodfill(face, xy=(0, 0),
                         value=get_corner_color(Image.open(random_file_from_dir(background_color_folder))))
    face.save(output_file_name)


if __name__ == '__main__':
    generate_face()
