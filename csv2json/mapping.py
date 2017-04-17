from collections import namedtuple

Mapping = namedtuple('Mapping', ['name', 'type'])

def default(header):
    return [Mapping(name, str) for name in header]

def do_mapping(line):
    name = line.split('=')[0]
    field_type = line.split('=')[1]
    return Mapping(name,
                   int if field_type[0] == 'int' else
                   str if line.split('=')[1] == 'string' else
                   float if line.split('=')[1] == 'float' else
                   mybool if line.split('=')[1] == 'bool' else None)


def read_mapping(filename):
    with open(filename) as f:
        return [do_mapping(line.strip()) for line in f if len(line.strip())]

