import argparse
from csv2json.mapping import read_mapping
from csv2json.main import validate_file, parse_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('mapping', help='Mapping file')
    parser.add_argument('data', help='Data file')
    parser.add_argument('--validate',
                        help='Validates given data file with mapping,'
                        'no data parsing done',
                        action='store_true')
    args = parser.parse_args()


    mapping = read_mapping(args.mapping)
    validated = validate_file(args.data, mapping)
#    if args.validate:
#         validated

    print(parse_file(args.data, mapping))
