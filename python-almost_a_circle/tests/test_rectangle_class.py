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
    
    def test_rectangle_area(self):
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(4, 5)
        self.assertEqual(r2.area(), 20)

    def test_rectangle_display(self):
        r1 = Rectangle(2, 2)
        self.assertEqual(r1.display(), None)

        r2 = Rectangle(3, 3, 1, 1)
        self.assertEqual(r2.display(), None)

    def test_rectangle_str(self):
        r1 = Rectangle(4, 5, 6, 7, 8)
        self.assertEqual(str(r1), "[Rectangle] (8)  6/7 - 4/5")

    def test_rectangle_update(self):
        r1 = Rectangle(1, 2)
        r1.update(2)
        self.assertEqual(r1.id, 2)

        r2 = Rectangle(3, 4, 5, 6, 7)
        r2.update(8, 9, 10, 11, 12)
        self.assertEqual(r2.id, 8)
        self.assertEqual(r2.width, 9)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 11)
        self.assertEqual(r2.y, 12)

        r3 = Rectangle(1, 1)
        r3.update(id=2, width=3, height=4, x=5, y=6)
        self.assertEqual(r3.id, 2)
        self.assertEqual(r3.width, 3)
        self.assertEqual(r3.height, 4)
        self.assertEqual(r3.x, 5)
        self.assertEqual(r3.y, 6)

if __name__ == '__main__':
    unittest.main()