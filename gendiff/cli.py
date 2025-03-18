import argparse


def prepare_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
        )
    parser.add_argument('first_file', type=str, help='')
    parser.add_argument('second_file', type=str, help='')
    parser.add_argument(
        '-f', '--format',
        type=str,
        default='stylish',
        help='output format (default: "stylish")'
        )
    args = parser.parse_args()
#    path_name_file1 = args.first_file
#    path_name_file2 = args.second_file
#    out_format = args.format
    return args.first_file, args.second_file, args.format
