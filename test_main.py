import unittest

class TestStudentManagement(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(1 + 2, 3)

    def test_upper(self):
        self.assertEqual("python".upper(), "PYTHON")

if __name__ == "__main__":
    unittest.main()