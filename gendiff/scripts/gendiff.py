#!/usr/bin/env python3
from gendiff.cli import prepare_arguments
from gendiff.result import generate_diff


def main():
    path_name_file1, path_name_file2, format_name = prepare_arguments()
    print(generate_diff(path_name_file1, path_name_file2, format_name))


if __name__ == '__main__':
    main()
