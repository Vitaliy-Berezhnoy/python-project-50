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
    out_format = args.format
    print(dir_and_name_file1)
    print(dir_and_name_file2)
    print(out_format)
    generate_diff(dir_and_name_file1, dir_and_name_file2)


def generate_diff(name_file1, name_file2):
    file1 = json.load(open(name_file1))
    file2 = json.load(open(name_file2))
    print(file1)
    print(file2)
