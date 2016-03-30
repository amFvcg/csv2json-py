import json
from collections import namedtuple

Mapping = namedtuple('Mapping', ['name', 'type'])


def mybool(val):
    return True if val in ['y', 'Y', '1']\
        else False if val in ['n', 'N', '0']\
        else None


def do_mapping(line):
    return Mapping(line.split('=')[0],
                   int if line.split('=')[1] == 'int' else
                   str if line.split('=')[1] == 'string' else
                   mybool if line.split('=')[1] == 'bool' else None)


def read_mapping(filename):
    with open(filename) as f:
        return [do_mapping(line.strip()) for line in f if len(line.strip())]


def validate_items(items, mapping):
    if len(items) != len(mapping):
        return False
    try:
        return all([True for i in
                    map(lambda x, y: x.type(y), mapping, items)])
    except ValueError:
        return False


def validate_file(filename, mapping):
    with open(filename) as f:
        return all([validate_items(line.split(';'), mapping) for line in f])


def parse_items(items, mapping):
    return dict([(key, value) for (key, value)
                in map(lambda x, y: (x.name, x.type(y)), mapping, items)])


def parse_file(filename, mapping):
    with open(filename) as f:
        return json.dumps(
            [parse_items([item.strip() for item in line.split(';')
                         if len(item.strip())], mapping)
             for line in f])
