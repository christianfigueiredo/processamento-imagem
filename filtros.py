from PIL import Image, ImageFilter
import os

DATA_DIR = os.path.join('filtros','data')

img = Image.open(os.path.join(DATA_DIR, 'youtube_space.jpg'))

img.show()
