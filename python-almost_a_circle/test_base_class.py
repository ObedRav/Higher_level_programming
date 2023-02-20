import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_unique_id(self):
        """
        Tests that each instance of Base has a unique ID.
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b1.id, b3.id)
        self.assertNotEqual(b2.id, b3.id)

    def test_custom_id(self):
        """
        Tests that an instance of Base can be created with a custom ID.
        """
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_no_id(self):
        """
        Tests that an instance of Base is assigned a unique ID if no ID is provided.
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

if __name__ == '__main__':
    unittest.main()
