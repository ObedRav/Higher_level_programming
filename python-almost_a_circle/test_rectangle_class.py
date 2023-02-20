import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_constructor(self):
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(10, 20, 30, 40, 1)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 20)
        self.assertEqual(r2.x, 30)
        self.assertEqual(r2.y, 40)
        self.assertEqual(r2.id, 1)

    def test_setters(self):
        r1 = Rectangle(10, 20)
        r1.width = 30
        r1.height = 40
        r1.x = 50
        r1.y = 60
        self.assertEqual(r1.width, 30)
        self.assertEqual(r1.height, 40)
        self.assertEqual(r1.x, 50)
        self.assertEqual(r1.y, 60)

if __name__ == '__main__':
    unittest.main()