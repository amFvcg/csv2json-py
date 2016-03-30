from collections import namedtuple

Mapping = namedtuple('Mapping', ['name', 'type'])


def mybool(val):
    return True


def do_mapping(lines):
    return [Mapping(line.split('=')[0],
                    int if line.split('=')[1] == 'int' else
                    str if line.split('=')[1] == 'string' else
                    mybool if line.split('=')[1] == 'bool' else None)
            for line in lines]


def read_mapping(filename):
    with open(filename) as f:
        return do_mapping(f)
