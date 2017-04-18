import argparse
from csv2json.mapping import read_mapping
from csv2json.main import validate_file, parse_file
import csv2json.mapping


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('data', help='Data file')
    parser.add_argument('--validate',
                        help='Validates given data file with mapping,'
                        'no data parsing done',
                        action='store_true')
    parser.add_argument('--delimiter',default=',')
    parser.add_argument('--mapping', help='Mapping file')
    args = parser.parse_args()

    if args.mapping:
        mapping = read_mapping(args.mapping)
    else:
        with open(args.data) as f:
            header = f.readline().strip().split(args.delimiter)
        mapping = csv2json.mapping.default(header)
#    validated = validate_file(args.data, mapping, args.delimiter)
#    if args.validate:
#         validated

    with open(args.data) as fin,\
         open(args.data+'.json', 'w') as fout:
        next(fin)
        parse_file(fin, fout, mapping, args.delimiter)

if __name__ == '__main__':
    main()
