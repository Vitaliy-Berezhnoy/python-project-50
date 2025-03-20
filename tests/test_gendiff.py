import os

from gendiff.result import generate_diff

path = './tests/test_data'
path_file1_json = os.path.join(path, 'file1.json')
path_file2_json = os.path.join(path, 'file2.json')
path_file1_yaml = os.path.join(path, 'file1.yaml')
path_file2_yml = os.path.join(path, 'file2.yml')
path_correct_stylish = os.path.join(path, 'correct_stylish.txt')
path_correct_plain = os.path.join(path, 'correct_plain.txt')
path_correct_json = os.path.join(path, 'correct_json.txt')


def test_generate_diff_stylish():
    expected = open(path_correct_stylish).read()
    actual = generate_diff(path_file1_json, path_file2_json)
    assert actual == expected
    actual = generate_diff(path_file1_yaml, path_file2_yml, 'stylish')
    assert actual == expected


def test_generate_diff_plain():
    expected = open(path_correct_plain).read()
    actual = generate_diff(path_file1_json, path_file2_yml, 'plain')
    assert actual == expected


def test_generate_diff_json():
    expected = open(path_correct_json).read()
    actual = generate_diff(path_file1_yaml, path_file2_json, 'json')
    assert actual == expected
