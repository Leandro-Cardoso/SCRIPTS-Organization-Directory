import json
import os

# LOAD CONFIGs:
config_file_path = './directory_organizer/config.json'
with open(config_file_path) as config_file:
    configs = json.load(config_file)
    config_file.close()

# CREATE FILEs LIST:
directory_path = configs['directory_path']
files = os.listdir(directory_path)
print(files, '\n\n')

# IMAGE VARs:
image_formats = configs['image_formats']
image_directory_name = configs['image_directory_name']

# VERIFY, CREATE DIR AND MOVE:
for file in files:
    file_path = os.path.join(directory_path, file)
    # IS IMAGE?:
    for format in image_formats:
        if f'.{format}' in file:
            new_directory_path = os.path.join(directory_path, image_directory_name)
            os.mkdir(new_directory_path)
            new_path = os.path.join(new_directory_path, file)
            os.replace(file_path, new_path)
