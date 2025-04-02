import io
import sys
import unittest
from source.print_field_as_table import print_field_as_table


class TestPrintFieldAsTable(unittest.TestCase):
    def test_with_valid_field(self):
        field = [
            [1, 1, 1, 0, 1],
            [0, 1, 0, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1],
        ]
        expected_output = (
            "   A B C D E\n\n"
            "1  1 1 1 0 1\n"
            "2  0 1 0 1 1\n"
            "3  1 0 1 1 1\n"
            "4  1 1 1 0 1\n"
            "5  1 1 1 1 1\n\n"
        )

        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_field_as_table(field)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_with_empty_field(self):
        field = []
        expected_output = "   A B C D E\n\n\n"

        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_field_as_table(field)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_with_non_integer_values(self):
        field = [
            ["X", "O", "X", "O", "X"],
            ["O", "X", "O", "X", "O"],
            ["X", "O", "X", "O", "X"],
            ["O", "X", "O", "X", "O"],
            ["X", "O", "X", "O", "X"],
        ]
        expected_output = (
            "   A B C D E\n\n"
            "1  X O X O X\n"
            "2  O X O X O\n"
            "3  X O X O X\n"
            "4  O X O X O\n"
            "5  X O X O X\n\n"
        )

        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_field_as_table(field)
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
