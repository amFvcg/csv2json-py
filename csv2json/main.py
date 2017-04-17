import json


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
