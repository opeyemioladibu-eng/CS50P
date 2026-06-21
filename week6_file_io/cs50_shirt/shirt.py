import sys
from PIL import Image, ImageOps
import PIL
import os


#if the user does not specify exactly two command line argument
if len(sys.argv) >3:
    sys.exit("Too many command-line arguments!")
elif len(sys.argv) <3:
    sys.exit("Too few command-line arguments!")

#if the input and output names do not end in .jpg,.jpeg,or .png
valid_extensions = (".jpg",".png", ".jpeg")
if not sys.argv[1].casefold().endswith(valid_extensions):
    sys.exit("wrong format!")
if not sys.argv[2].casefold().endswith(valid_extensions):
    sys.exit("Wrong format!") 

#if the input name does not have the same extension as output name
input = os.path.splitext(sys.argv[1])[1].casefold()
output = os.path.splitext(sys.argv[2])[1].casefold()
if input != output:
    sys.exit("Extension don't match!")

#if specified input does not exist
if not os.path.exists(sys.argv[1]):
    sys.exit("Input does not exist!")
 

#open
try:
    shirt = Image.open("shirt.png")
except FileNotFoundError:
    sys.exit("shirt.png not found")

#open image i.e shirt.png
open_image = Image.open(sys.argv[1])

#resize
size = shirt.size
input_image = ImageOps.fit(open_image, size)

#paste shirt onto input image 
input_image.paste(shirt, (0,0), shirt)

# save result 
input_image.save(sys.argv[2])