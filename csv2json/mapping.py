from collections import namedtuple

Mapping = namedtuple('Mapping', ['name', 'type'])

def default(header):
    return [Mapping(name, str) for name in header]

def do_mapping(line):
    import csv2json.types as t
    name = line.split('=')[0]
    field_type = line.split('=')[1]
    return Mapping(name,
                   int if field_type == 'int' else
                   str if field_type == 'string' else
                   float if field_type == 'float' else
                   t.bool if field_type == 'bool' else
                   None)


def read_mapping(filename):
    with open(filename) as f:
        return [do_mapping(line.strip()) for line in f if len(line.strip())]

