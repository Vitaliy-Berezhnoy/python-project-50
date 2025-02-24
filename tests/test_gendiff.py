from diff_calc.gendiff import generate_diff


def test_generate_diff():
    path_file1 = './tests/test_data/file1.json'
    path_file2 = './tests/test_data/file2.json'
    path_expected = './tests/test_data/correct_result.txt'
    actual = generate_diff(path_file1, path_file2)
    expected = open(path_expected).read()
    assert actual == expected
    path_file1 = './tests/test_data/file1.yaml'
    path_file2 = './tests/test_data/file2.yaml'
    actual = generate_diff(path_file1, path_file2)
    assert actual == expected
