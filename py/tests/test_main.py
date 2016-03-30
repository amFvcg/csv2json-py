from unittest import TestCase


class TestMain(TestCase):
    def test_mybool(self):
        from main import mybool
        self.assertTrue(mybool("Y"))

    def test_do_mapping(self):
        from main import do_mapping, Mapping, mybool
        lines = ['id=int', 'name=string', 'mybool=bool']
        self.assertListEqual([Mapping('id', int),
                              Mapping('name', str),
                              Mapping('mybool', mybool)],
                             do_mapping(lines))
