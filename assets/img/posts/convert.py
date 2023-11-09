import os
from PIL import Image

# Define the directory where images are saved
image_directory = './'
# Listing the .png files in the directory
image_files = [file for file in os.listdir(image_directory) if file.endswith('.png')]

# Convert each .png file to .jpg
converted_files = []
for image_file in image_files:
    # Open the image file
    with Image.open(os.path.join(image_directory, image_file)) as img:
        # Define the new filename
        filename_wo_extension = os.path.splitext(image_file)[0]
        new_filename = f"{filename_wo_extension}.jpg"
        # Convert the image to RGB format and save as a .jpg
        rgb_img = img.convert('RGB')
        rgb_img.save(os.path.join(image_directory, new_filename))
        # Append the new filename to the list
        converted_files.append(new_filename)

converted_files
