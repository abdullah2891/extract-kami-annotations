import unittest

class TestExample(unittest.TestCase):
    def setUp(self):
        """
        This method is called before every test.
        Use it to set up test-specific conditions.
        """
        self.example_variable = 42  # Example setup variable
        self.example_list = [1, 2, 3]

    def test_example_variable(self):
        """Test that the example variable is correctly set."""
        self.assertEqual(self.example_variable, 42, "The example_variable should be 42")

    def test_example_list(self):
        """Test that the example list contains the expected values."""
        self.assertIn(2, self.example_list, "The value 2 should be in the example_list")
        self.assertEqual(len(self.example_list), 3, "The example_list should contain 3 elements")


if __name__ == '__main__':
    unittest.main()

