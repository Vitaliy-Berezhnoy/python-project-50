import argparse
import json


def prepare_arguments():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')
    parser.add_argument('-f', '--format', type=str, default='.json', help='set format of output')
    args = parser.parse_args()
    dir_and_name_file1 = args.first_file
    dir_and_name_file2 = args.second_file
#    out_format = args.format
    generate_diff(dir_and_name_file1, dir_and_name_file2)


def generate_diff(name_file1: str, name_file2: str):
    file1 = json.load(open(name_file1))
    file2 = json.load(open(name_file2))
    print(file1)
    print(file2)

    def inner(key: str):
        if key not in file2:
            return f'  - {key}: {file1[key]}'
        if file1[key] == file2[key]:
            return f'    {key}: {file1[key]}'
        return f'  -{key}: {file1[key]}\n  +{key}: {file2[key]}'

    key_file1 = sorted(file1)
    key_file2 = sorted(file2)
    out_list = ['{']
    out_list.extend(list(map(inner, key_file1)))
    new_key = set(key_file2) - set(key_file1)
#    new_key = filter(lambda key: key not in key_file1, key_file2)
    out_list.extend(list(map(lambda key: f'  +{key}: {file2[key]}', new_key)))
    out_list.append('}')
    print('\n'.join(out_list))
    return '\n'.join(out_list)    
