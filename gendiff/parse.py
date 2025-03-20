import json
import os

import yaml


def load_file(path_name_file):
    #    extension = pathlib.PurePath(path_name_file).suffix
    _, extension = os.path.splitext(path_name_file)
    if extension == '.json':
        with open(path_name_file, 'r') as f:
            return json.load(f)
    if extension == '.yaml' or '.yml':
        with open(path_name_file, 'r') as f:
            return yaml.safe_load(f)
