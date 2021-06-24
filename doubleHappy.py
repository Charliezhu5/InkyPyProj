#!/usr/bin/env python

import os
from PIL import Image
from inky.auto import auto


print("""Inky pHAT/wHAT: Double Happy

Displays the Inky pHAT/wHAT Double Happy.

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

# Pick the correct logo image to show depending on display resolution/colour

img = Image.open(os.path.join(PATH, "phat/resources/test.png"))

# Display the image

inky_display.set_image(img)
inky_display.show()
