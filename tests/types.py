from unittest import TestCase


class TestMain(TestCase):
    def test_bool_nonBoolCharacter_exceptionThrown(self):
        from types import bool
        self.assertRaises(ValueError, bool("Z"))

    def test_bool_boolCharacter_trueReturned(self):
        from types import bool
        self.assertTrue(bool("Y"))
        self.assertTrue(bool("y"))
        self.assertTrue(bool("1"))

    def test_bool_boolCharacter_falseReturned(self):
        from types import bool
        self.assertFalse(bool("N"))
        self.assertFalse(bool("n"))
        self.assertFalse(bool("0"))

    def test_nullable_emptyString_returnsNone(self):
        from types import nullable
        self.assertIsNone(nullable(str("")))

    def test_nullable_nonemptyString_returnsNonEmptyString(self):
        from types import nullable
        s = 'ABC'
        self.assertEqual(s, nullable(str(s)))
