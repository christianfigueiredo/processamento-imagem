from PIL import Image
import os

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

def in_path(filename):
    return os.path.join(INPUT_FOLDER,filename)

image = Image.open(in_path("campeon.jpg"))
print(image.getpixel((500,500)))

image.show()