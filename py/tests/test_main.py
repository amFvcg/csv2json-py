from unittest import TestCase


class TestMain(TestCase):
    def test_mybool(self):
        from main import mybool
        self.assertTrue(mybool("Y"))
        self.assertTrue(mybool("y"))
        self.assertTrue(mybool("1"))
        self.assertFalse(mybool("N"))
        self.assertFalse(mybool("n"))
        self.assertFalse(mybool("0"))

    def test_do_mapping(self):
        from main import do_mapping, Mapping, mybool
        lines = ['id=int', 'name=string', 'mybool=bool']
        parsed_lines = [do_mapping(line) for line in lines]
        self.assertListEqual([Mapping('id', int),
                              Mapping('name', str),
                              Mapping('mybool', mybool)],
                             parsed_lines)

    def test_validate_items(self):
        from main import validate_items, mybool, Mapping
        items = ['1', 'some string', 'N']
        mapping = [Mapping('id', int),
                   Mapping('name', str),
                   Mapping('mybool', mybool)]
        self.assertTrue(validate_items(items, mapping))

    def test_validate_items_fail(self):
        from main import validate_items, mybool, Mapping
        items = ['1a', 'some string', 'N']
        mapping = [Mapping('id', int),
                   Mapping('name', str),
                   Mapping('mybool', mybool)]
        self.assertFalse(validate_items(items, mapping))

    def test_parse_items(self):
        from main import parse_items, mybool, Mapping
        items = ['1', 'some string', 'N']
        mapping = [Mapping('id', int),
                   Mapping('name', str),
                   Mapping('mybool', mybool)]
        self.assertDictEqual({'id': 1, 'name': 'some string', 'mybool': False},
                             parse_items(items, mapping))
