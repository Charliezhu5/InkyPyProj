import os
import argparse
from PIL import Image
from inky.auto import auto

print("""Inky pHAT/wHAT: Logo

Displays the Inky pHAT/wHAT logo.

""")

# Get the current path
PATH = os.path.dirname(__file__)

# Set up the Inky display
try:
    inky_display = auto(ask_user=True, verbose=True)
except TypeError:
    raise TypeError("You need to update the Inky library to >= v1.1.0")

try:
    inky_display.set_border(inky_display.BLACK)
except NotImplementedError:
    pass

# Command line arguments to determine number of cycles to run
parser = argparse.ArgumentParser()
parser.add_argument('--name', '-n', required=True, help="name of picture")
name = parser.parse_args().name

# Pick the correct logo image to show depending on parsed name

img = Image.open(os.path.join(PATH, f'phat/resources/{name}.png'))

# Display the logo image

inky_display.set_image(img)
inky_display.show()