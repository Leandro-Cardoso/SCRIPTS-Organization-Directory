import json
import os

# CREATE DIR AND MOVE FILES:
def mkdir_and_replace(formats, file, directory_path, directory_name):
    for format in formats:
        if f'.{format}' in file:
            file_path = os.path.join(directory_path, file)
            # mkdir:
            new_directory_path = os.path.join(directory_path, directory_name)
            if not os.path.exists(new_directory_path):
                os.mkdir(new_directory_path)
            # replace:
            new_path = os.path.join(new_directory_path, file)
            if not os.path.exists(new_path):
                os.replace(file_path, new_path)

# LOAD CONFIGs:
config_file_path = './directory_organizer/config.json'
with open(config_file_path) as config_file:
    configs = json.load(config_file)
    config_file.close()

# CREATE FILEs LIST:
directory_path = configs['directory_path']
files = os.listdir(directory_path)

# VERIFY, CREATE DIR AND MOVE:
for file in files:
    file_path = os.path.join(directory_path, file)
    # IS IMAGE?:
    mkdir_and_replace(formats = configs['image_formats'], file = file, directory_path = directory_path, directory_name = configs['image_directory_name'])
    # IS TEXT?:
    mkdir_and_replace(formats = configs['text_formats'], file = file, directory_path = directory_path, directory_name = configs['text_directory_name'])
    # IS APP?:
    mkdir_and_replace(formats = configs['app_formats'], file = file, directory_path = directory_path, directory_name = configs['app_directory_name'])
    # IS AUDIO?:
    # IS VIDEO?:
