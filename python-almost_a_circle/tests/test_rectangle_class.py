import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect = Rectangle(10, 20)

    def test_init(self):
        self.assertIsInstance(self.rect, Rectangle)
        self.assertEqual(self.rect.width, 10)
        self.assertEqual(self.rect.height, 20)
        self.assertEqual(self.rect.x, 0)
        self.assertEqual(self.rect.y, 0)
        self.assertEqual(self.rect.id, 5)

    def test_setters(self):
        self.rect.width = 30
        self.assertEqual(self.rect.width, 30)
        self.assertRaises(TypeError, setattr, self.rect, "width", "30")
        self.assertRaises(ValueError, setattr, self.rect, "width", 0)
        self.rect.height = 40
        self.assertEqual(self.rect.height, 40)
        self.assertRaises(TypeError, setattr, self.rect, "height", "40")
        self.assertRaises(ValueError, setattr, self.rect, "height", 0)
        self.rect.x = 50
        self.assertEqual(self.rect.x, 50)
        self.assertRaises(TypeError, setattr, self.rect, "x", "50")
        self.assertRaises(ValueError, setattr, self.rect, "x", -1)
        self.rect.y = 60
        self.assertEqual(self.rect.y, 60)
        self.assertRaises(TypeError, setattr, self.rect, "y", "60")
        self.assertRaises(ValueError, setattr, self.rect, "y", -1)

    def test_area(self):
        self.assertEqual(self.rect.area(), 200)
        self.rect.width = 5
        self.assertEqual(self.rect.area(), 100)

    def test_display(self):
        self.rect.display()

    def test_str(self):
        self.assertEqual(str(self.rect), "[Rectangle] (7)  0/0 - 10/20")

    def test_update(self):
        self.rect.update(2, 30, 40, 50, 60)
        self.assertEqual(self.rect.id, 2)
        self.assertEqual(self.rect.width, 30)
        self.assertEqual(self.rect.height, 40)
        self.assertEqual(self.rect.x, 50)
        self.assertEqual(self.rect.y, 60)

        self.rect.update(width=5, y=10)
        self.assertEqual(self.rect.width, 5)
        self.assertEqual(self.rect.y, 10)

        self.rect.update(2, 30, 40, 50, 60, 70, 80, 90)
        self.assertEqual(self.rect.id, 2)
        self.assertEqual(self.rect.width, 30)
        self.assertEqual(self.rect.height, 40)
        self.assertEqual(self.rect.x, 50)
        self.assertEqual(self.rect.y, 60)

    def test_errors(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            rectangle = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            ectangle = Rectangle(1, 2, 3, "4")
        with self.assertRaises(TypeError):
            rectangle = Rectangle(1, 2, "3", 4)

        with self.assertRaises(ValueError):
            rectangle = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            rectangle = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            rectangle = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            rectangle = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            rectangle = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            rectangle = Rectangle(1, 2, 3, -4)

if __name__ == '__main__':
    unittest.main()