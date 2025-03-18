from gendiff.formatters.json import make_format_json
from gendiff.formatters.plain import make_format_plain
from gendiff.formatters.stylish import (
    OFFSET,
    SPACE,
    SYMBOL,
    make_format_stylish,
)
from gendiff.parse import load_file


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
            return make_format_stylish(diff, OFFSET, SPACE, SYMBOL)
        case 'plain':
            return make_format_plain(diff)
        case 'json':
            return make_format_json(diff)
