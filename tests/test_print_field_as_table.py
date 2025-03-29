import unittest
from io import StringIO
import sys

from source.print_field_as_table import print_field_as_table


class TestPrintField(unittest.TestCase):
    def test_print_field_as_table(self):
        field = [
            [1, 1, 1, 0, 1],
            [0, 1, 0, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1],
        ]

        expected_output = """   A B C D E\n
1  1 1 1 0 1
2  0 1 0 1 1
3  1 0 1 1 1
4  1 1 1 0 1
5  1 1 1 1 1
"""

        captured_output = StringIO()
        sys.stdout = captured_output
        print_field_as_table(field)
        sys.stdout = sys.__stdout__  # Reset stdout

        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
