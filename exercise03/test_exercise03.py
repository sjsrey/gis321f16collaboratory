import unittest
from exercise03 import lines_in_file, get_line, fields_in_line
from exercise03 import n_fields_in_line, longest_field_in_line


class Test_exercise03(unittest.TestCase):
    """
    Below are a series of tests, some of which will fail.

    In this assignment you will correct the failing tests.
    """

    def setUp(self):
        """
        This is called before any other tests so it is a good place to put
        objects that can be reused across the tests that follow
        """

        self.fname = 'data.csv'

    def test_lines_in_file(self):
        lines = lines_in_file(self.fname)
        self.assertIsInstance(lines, list)

    def test_get_line(self):
        line_2 = '2,Madang,Madang,Papua New Guinea,MAG,AYMD,-5.207083,145.7887,20,10,U\n'
        self.assertEqual(get_line(self.fname, 2), line_2)

    def test_fields_in_line(self):
        fields =['2', 'Madang', 'Madang', 'Papua New Guinea', 'MAG', 'AYMD', '-5.207083', '145.7887', '20', '10', 'U']
        line_2 = get_line(self.fname, 2)
        line_2_fields = fields_in_line(line_2)
        self.assertEqual(line_2_fields, fields)

    def test_n_fields_in_line(self):
        line_2 = get_line(self.fname, 2)
        nw = n_fields_in_line(line_2)
        self.assertEqual(nw, 11)

    def test_longest_field_in_line(self):
        line_2 = get_line(self.fname, 2)
        longest = longest_field_in_line(line_2)
        self.assertEqual(longest, 'airport_id')

    if __name__ == '__main__':
        unittest.main()
