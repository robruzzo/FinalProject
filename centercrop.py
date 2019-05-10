#!/usr/bin/python3

import os

from PIL import Image

INPUT_DIR = '/floyd/home/data/input/'
OUTPUT_DIR = '/floyd/home/data/input/cropped/'
TOLERANCE = 11

def process(file):
    # Print out some file information
    image = Image.open(file)
    width = image.size[0]
    height = image.size[1]
    
    #define crop size
    crop_size_x = 40 # x axis pixels -center
    crop_size_y = 40 # y axis pixels -center
   
    #Set up  box bounds
    crop_x_start = (width-crop_size_x)//2
    crop_x_end =(crop_x_start + crop_size_x)
    crop_y_start = (height-crop_size_y)//2
    crop_y_end =(crop_y_start + crop_size_y)

    # Crop image
    print("Cropping image...")
    cropped_image = image.crop((crop_x_start, crop_y_start, crop_x_end, crop_y_end))

    # Save image to output dir
    file_name, file_ext = os.path.splitext(file)
    output_file_name = os.path.basename(file_name) + file_ext
    output_file_path = os.path.join(os.getcwd(), OUTPUT_DIR, output_file_name)
    print("Saving image to " + output_file_path)
    cropped_image.save(output_file_path)

def main():
    image_exts = [ '.tif' ]
    input_dir = os.path.join(os.getcwd(), INPUT_DIR)
    output_dir = os.path.join(os.getcwd(), OUTPUT_DIR)

    # Create output directory, if not present
    try:
        os.stat(output_dir)
    except:
        os.mkdir(output_dir)

    # Iterate over working directory
    for file in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file)
        file_name, file_ext = os.path.splitext(file_path)

        # Check if file is an image file
        if file_ext not in image_exts:
            print("Skipping " + file + " (not an image file)")
            continue
        else:
            print()
            print("Processing " + file + "...")
            process(file_path)

if __name__ == '__main__':
    main()