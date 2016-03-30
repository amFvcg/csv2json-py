import argparse
from main import read_mapping, validate_file, parse_file

parser = argparse.ArgumentParser()
parser.add_argument('mapping', help='Mapping file')
parser.add_argument('data', help='Data file')
parser.add_argument('--validate',
                    help='Validates given data file with mapping,'
                    'no data parsing done',
                    action='store_true')
args = parser.parse_args()


if __name__ == "__main__":
    mapping = read_mapping(args.mapping)
    print(validate_file(args.data, mapping))
    print(parse_file(args.data, mapping))
