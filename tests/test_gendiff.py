import os

from diff_calc.gendiff import generate_diff


def test_generate_diff():
    path_file1 = os.path.join('./tests/test_data', 'file1.json')
    path_file2 = os.path.join('./tests/test_data', 'file2.json')
    path_expected = os.path.join(
        './tests/test_data', 'correct_stylish.txt'
         )
    actual = generate_diff(path_file1, path_file2)
    expected = open(path_expected).read()
    assert actual == expected
    path_file1 = os.path.join('./tests/test_data', 'file1.yaml')
    path_file2 = os.path.join('./tests/test_data', 'file2.yaml')
    actual = generate_diff(path_file1, path_file2)
    assert actual == expected
    path_expected = os.path.join(
        './tests/test_data', 'correct_plain.txt'
        )
    actual = generate_diff(path_file1, path_file2, 'plain')
    expected = open(path_expected).read()
    assert actual == expected
    path_expected = os.path.join(
        './tests/test_data', 'correct_json.txt'
    )
    actual = generate_diff(path_file1, path_file2, 'json')
    expected = open(path_expected).read()
    assert actual == expected

