from unittest import TestCase


class TestMain(TestCase):
    def test_do_mapping(self):
        from csv2json.mapping import do_mapping, Mapping
        from csv2json.types import bool
        lines = ['id=int', 'name=string', 'bool=bool']
        parsed_lines = [do_mapping(line) for line in lines]
        self.assertListEqual([Mapping('id', int),
                              Mapping('name', str),
                              Mapping('bool', bool)],
                             parsed_lines)

    def test_default(self):
        from csv2json.mapping import default
        header = ['Field1', 'Field2']
        self.assertListEqual([], [])

    def test_validate_items(self):
        from csv2json.main import validate_items
        from csv2json.mapping import Mapping
        from csv2json.types import bool

        items = ['1', 'some string', 'N']
        mapping = [Mapping('id', int),
                   Mapping('name', str),
                   Mapping('bool', bool)]
        self.assertTrue(validate_items(items, mapping))

    def test_validate_items_fail(self):
        from csv2json.main import validate_items
        from csv2json.mapping import Mapping
        from csv2json.types import bool

        items = ['1a', 'some string', 'N']
        mapping = [Mapping('id', int),
                   Mapping('name', str),
                   Mapping('bool', bool)]
        self.assertFalse(validate_items(items, mapping))

    def test_parse_items(self):
        from csv2json.main import parse_items
        from csv2json.mapping import Mapping
        from csv2json.types import bool

        items = ['1', 'some string', 'N']
        mapping = [Mapping('id', int),
                   Mapping('name', str),
                   Mapping('bool', bool)]
        self.assertDictEqual({'id': 1, 'name': 'some string', 'bool': False},
                             parse_items(items, mapping))
