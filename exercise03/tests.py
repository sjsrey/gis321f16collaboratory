import unittest

class Test_EX03(unittest.TestCase):
    """
    Below are a series of tests, some of which will fail.

    In this assignment you will correct the failing tests.
    """

    def setUp(self):
        """
        This is called before any other tests so it is a good place to put
        objects that can be reused across the tests that follow
        """

        self.string = 'GIS 321 Fall 2016'
        self.amp_del_string = '123&456&7.80&-40.1&42'

    def test_assert_truth(self):
        """
        A test that will pass
        """

        self.assertTrue(True)

    def test_assert_equality(self):
        """
        A test to check for equality
        """
        self.assertEqual(self.string, 'GIS 321 Fall 2016')

    def test_assert_string(self):
        """
        Check of our string attribute is of type `str`
        """
        self.assertTrue(type(self.string), str)

    def test_len(self):
        """
        This will fail as we are off somehow
        """
        s_len = len(self.string.split())
        self.assertEqual(s_len, 4)

    def test_false(self):
        """
        Testing for false
        """
        s_len = len(self.string.split())
        self.assertFalse(s_len == 5)

    def test_type_conversion(self):
        """
        A series of tests to validate type conversion operations
        """

        i = 1
        self.assertTrue(type(i) == int)
        self.assertTrue(isinstance(i, int))
        i = float(i)
        self.assertTrue(isinstance(i, float))
        i = str(i)
        self.assertTrue(isinstance(i, str))

    def test_list_len(self):
        """
        Testing length of a list
        """
        l = [1, 2, 3]
        self.assertTrue(len(l), 3)

    def test_string_split(self):
        """
        Testing the splitting of string
        """
        ss = self.string.split()
        self.assertTrue(len(ss), 4)

        ss = self.amp_del_string.split()
        self.assertTrue(len(ss), 1)

        ss = self.amp_del_string.split('&')
        self.assertTrue(len(ss), 5)

    def test_readlines(self):
        with open('data.csv') as f:
            lines = f.readlines()
        self.assertIsInstance(lines, list)


if __name__ == '__main__':
    unittest.main()
