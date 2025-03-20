from gendiff.diff import calculate_diff
from gendiff.formatters.json import make_format_json
from gendiff.formatters.plain import make_format_plain
from gendiff.formatters.stylish import (
    OFFSET,
    SPACE,
    SYMBOL,
    make_format_stylish,
)
from gendiff.parse import load_file


def generate_diff(path_name_file1, path_name_file2, format_name='stylish'):
    data1 = load_file(path_name_file1)
    data2 = load_file(path_name_file2)
    diff = calculate_diff(data1, data2)
    if format_name == 'stylish':
        return make_format_stylish(diff, OFFSET, SPACE, SYMBOL)
    if format_name == 'plain':
        return make_format_plain(diff)
    if format_name == 'json':
        return make_format_json(diff)