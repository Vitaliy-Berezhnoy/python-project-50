import argparse
import json
import os
import pathlib

import yaml

from diff_calc.formatters.stylish import (
    OFFSET,
    SPACE,
    SYMBOL,
    making_a_stylish_conclusion,
)


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
    path_name_file1 = pathlib.Path(args.first_file)
    path_name_file2 = args.second_file
#    out_format = args.format
    return generate_diff(path_name_file1, path_name_file2)


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


def calculate_diff(in_data1, in_data2) -> dict:
    
    def inner(key, data1, data2) -> dict:
        if key not in data1:
            return {'status': 'add', 'val': data2[key]}
        if key not in data2:
            return {'status': 'del', 'val': data1[key]}
        if isinstance(data1[key], dict) and isinstance(data2[key], dict):
            return {
                'status': 'nested',
                'val': calculate_diff(data1[key], data2[key])
                }
        if data1[key] == data2[key]:
            return {'status': 'match', 'val': data1[key]}
        return {'status': 'mod', 'val': data1[key], 'val2': data2[key]}
    
    all_key = sorted(in_data1 | in_data2)
    diff = {}   
    for key in all_key:
        diff[key] = inner(key, in_data1, in_data2)
    return diff


def generate_diff(path_name_file1, path_name_file2, format_name='stylish'):
    data1 = load_file(path_name_file1)
    data2 = load_file(path_name_file2)
    diff = calculate_diff(data1, data2)
    match format_name:
        case 'stylish':
            r = making_a_stylish_conclusion(diff, OFFSET, SPACE, SYMBOL)
            print(r)
            return r
