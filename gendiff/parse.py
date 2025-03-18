import json
import os

import yaml


def load_file(path_name_file):
    #    extension = pathlib.PurePath(path_name_file).suffix
    _, extension = os.path.splitext(path_name_file)
    match extension:
        case '.json':
            with open(path_name_file, 'r') as f:
                data = json.load(f)
        case '.yaml' | '.yml':
            with open(path_name_file, 'r') as f:
                data = yaml.safe_load(f)
    return data
