import argparse
import json

import yaml

# from itertools import chain


def prepare_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
        )
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')
    parser.add_argument(
        '-f', '--format',
        type=str,
        default='.json',
        help='set format of output'
        )
    args = parser.parse_args()
    path_name_file1 = args.first_file
    path_name_file2 = args.second_file
#    out_format = args.format
    print(generate_diff(path_name_file1, path_name_file2))


def generate_diff(path_name_file1: str, path_name_file2: str):
    if path_name_file1.endswith('.json'):
        file1 = json.load(open(path_name_file1))
        file2 = json.load(open(path_name_file2))
    else:
        with open(path_name_file1, 'r') as file_1:
            file1 = yaml.safe_load(file_1)
        with open(path_name_file2, 'r') as file_2:
            file2 = yaml.safe_load(file_2)
    print(file1)
    print(file2)

    def inner(key: str):
        if key not in file2:
            return f'  - {key}: {file1[key]}'
        if file1[key] == file2[key]:
            return f'    {key}: {file1[key]}'
        return f'  - {key}: {file1[key]}\n  + {key}: {file2[key]}'

    key_file1 = sorted(file1)
    key_file2 = sorted(file2)
    new_key = set(key_file2) - set(key_file1)
#    new_key = filter(lambda key: key not in key_file1, key_file2)
    out_list = ['{']
    out_list.extend(list(map(inner, key_file1)))  
    out_list.extend(list(map(lambda key: f'  + {key}: {file2[key]}', new_key)))
    out_list.append('}')
    result = '\n'.join(out_list)
    result = result.replace('True', 'true')
    result = result.replace('False', 'false')
    return result

#    def inner(key: str):
#        if key not in file2:
#            return [(f'- {key}', file1[key])]
#        if file1[key] == file2[key]:
#            return [(f'  {key}', file1[key])]
#        return [(f'- {key}', file1[key]), (f'+ {key}', file2[key])]
#
#    key_file1 = sorted(file1)
#    key_file2 = sorted(file2)
#    out_list = list(map(inner, key_file1))
#    new_key = set(key_file2) - set(key_file1)
#    out_list.extend(list(map(lambda key: [(f'+ {key}', file2[key])], new_key)))
#    out_dict = dict(chain(*out_list))
#    print(out_list)
#    print(out_dict)
#    result = json.dumps(out_dict, indent=2)
#    result = result.replace('"', '')
#    print(result)
#    return result
