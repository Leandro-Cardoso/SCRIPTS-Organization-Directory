import json
import os

# LOAD CONFIGs:
config_file_path = './directory_organizer/config.json'
with open(config_file_path) as config_file:
    configs = json.load(config_file)
    config_file.close()

print(configs)
