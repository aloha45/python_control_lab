# we want to convert a directory of all jpgs into all png files

# png are especially better for low color pics in development

from PIL import Image
import sys
import os

# we need to grab all of the images files and then make a new folder and put the converted files into that new folder

# use the sys to grab the first and second argument

image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)

# check if output folder exists and if not, create it we will use an os module

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through the Image folder and then covert images to .png

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    # put slash here if the user input does not have one after the directory
    cleaned_up = os.path.splitext(filename)[0]
    print(cleaned_up)
    img.save(f'{output_folder}{cleaned_up}.png', 'png')

print('hey all done')

