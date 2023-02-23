import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_init(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertIsNotNone(square.id)

    def test_size_property(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)


    def test_str(self):
        square = Square(5, 2, 3, 4)
        self.assertEqual(str(square), "[Square] (4) 2/3 - 5")

    def test_update(self):
        square = Square(5, 2, 3, 4)
        square.update(1, 10, 20, 30)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 20)
        self.assertEqual(square.y, 30)

        square.update(id=2, size=15, x=25, y=35)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 15)
        self.assertEqual(square.x, 25)
        self.assertEqual(square.y, 35)

    def test_to_dictionary(self):
        square = Square(5, 2, 3, 4)
        expected_dict = {"id": 4, "size": 5, "x": 2, "y": 3}
        self.assertDictEqual(square.to_dictionary(), expected_dict)

    def test_errors(self):
        with self.assertRaises(TypeError):
            square = Square("1")
        with self.assertRaises(TypeError):
            square = Square(1, "2")
        with self.assertRaises(TypeError):
            square = Square(1, 2, "4")

        with self.assertRaises(ValueError):
            square = Square(-1)
        with self.assertRaises(ValueError):
            square = Square(1, -2)
        with self.assertRaises(ValueError):
            square = Square(1, 2, -3)
        with self.assertRaises(ValueError):
            square = Square(0)

if __name__ == '__main__':
    unittest.main()