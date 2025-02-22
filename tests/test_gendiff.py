from pathlib import Path

from diff_calc.gendiff import generate_diff


def test_generate_diff():
    path_file1 = Path(__file__).parent / 'test_data' / 'file1.json'
    path_file2 = Path(__file__).parent / 'test_data' / 'file2.json'
    path_expected = Path(__file__).parent / 'test_data' / 'correct_result.txt'
    actual = generate_diff(path_file1, path_file2)
    expected = path_expected.read_text()
    assert actual == expected
