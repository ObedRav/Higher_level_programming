import unittest
import os
from unittest.mock import patch, mock_open
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
        self.assertGreaterEqual(self.rect.id, 1)

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
        rectangle1 = Rectangle(1, 2)
        self.assertEqual(rectangle1.display(), None)
        rectangle1 = Rectangle(1, 2, 3)
        self.assertEqual(rectangle1.display(), None)
        rectangle1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle1.display(), None)

    def test_str(self):
        self.assertGreaterEqual(str(self.rect), "[Rectangle] (10)  0/0 - 10/20")
        rectangle1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rectangle1.to_dictionary(), {'x': 3, 'y': 4, 'id': 26, 'height': 2, 'width': 1})

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
    
    def test_save_to_file(self):
        list_rectangles = [self.rect]
        with patch('builtins.open', mock_open()) as mock_file:
            Rectangle.save_to_file(list_rectangles)
            mock_file.assert_called_once_with('Rectangle.json', mode='w', encoding='utf-8')
            mock_file().write.assert_called_once_with('[{"x": 0, "y": 0, "id": 22, "height": 20, "width": 10}]')

        list_rectangles = []
        with patch('builtins.open', mock_open()) as mock_file:
            Rectangle.save_to_file(list_rectangles)
            mock_file.assert_called_once_with('Rectangle.json', mode='w', encoding='utf-8')
            mock_file().write.assert_called_once_with([])
        
        list_rectangles = None
        with patch('builtins.open', mock_open()) as mock_file:
            Rectangle.save_to_file(list_rectangles)
            mock_file.assert_called_once_with('Rectangle.json', mode='w', encoding='utf-8')
            mock_file().write.assert_called_once_with([])

        list_rectangles = [Rectangle(1, 2)]
        with patch('builtins.open', mock_open()) as mock_file:
            Rectangle.save_to_file(list_rectangles)
            mock_file.assert_called_once_with('Rectangle.json', mode='w', encoding='utf-8')
            mock_file().write.assert_called_once_with('[{"x": 0, "y": 0, "id": 23, "height": 2, "width": 1}]')


    def test_create_rectangle(self):
        rectangle_dict = {'id': 89}
        rectangle = Rectangle.create(**rectangle_dict)
        self.assertEqual(rectangle.__str__(), "[Rectangle] (89)  0/0 - 1/1")
        rectangle_dict = {'id': 89, 'width': 1}
        rectangle = Rectangle.create(**rectangle_dict)
        self.assertEqual(rectangle.__str__(), "[Rectangle] (89)  0/0 - 1/1")
        rectangle_dict = {'id': 89, 'width': 1, 'height': 2 }
        rectangle = Rectangle.create(**rectangle_dict)
        self.assertEqual(rectangle.__str__(), "[Rectangle] (89)  0/0 - 1/2")
        rectangle_dict = {'id': 89, 'width': 1, 'height': 2, 'x': 3}
        rectangle = Rectangle.create(**rectangle_dict)
        self.assertEqual(rectangle.__str__(), "[Rectangle] (89)  3/0 - 1/2")
        rectangle_dict = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        rectangle = Rectangle.create(**rectangle_dict)
        self.assertEqual(rectangle.__str__(), "[Rectangle] (89)  3/4 - 1/2")

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        # Save the list of rectangles to a file
        Rectangle.save_to_file(list_rectangles_input)

        # Load the list of rectangles from the file
        list_rectangles_output = Rectangle.load_from_file()

        # Check that the output list has the same length as the input list
        self.assertEqual(len(list_rectangles_input), len(list_rectangles_output))

        # Check that the rectangles in the output list have the same attributes as the rectangles in the input list
        for i in range(len(list_rectangles_input)):
            self.assertEqual(list_rectangles_input[i].to_dictionary(), list_rectangles_output[i].to_dictionary())

        # Delete the file
        os.remove("Rectangle.json")

    def test_display_without_x_y(self):
        # Create a rectangle object
        rectangle = Rectangle(3, 4)

        # Redirect the stdout to a buffer
        from io import StringIO
        buffer = StringIO()
        import sys
        sys.stdout = buffer

        # Call the display method
        rectangle.display()

        # Get the printed output from the buffer
        output = buffer.getvalue().strip()

        # Reset the stdout
        sys.stdout = sys.__stdout__

        # Check if the output matches the expected string
        expected_output = '###\n###\n###\n###'
        self.assertEqual(output, expected_output)

    def test_display_without_y(self):
                # Create a rectangle object
        rectangle = Rectangle(3, 4, 2)

        # Redirect the stdout to a buffer
        from io import StringIO
        buffer = StringIO()
        import sys
        sys.stdout = buffer

        # Call the display method
        rectangle.display()

        # Get the printed output from the buffer
        output = buffer.getvalue().strip()

        # Reset the stdout
        sys.stdout = sys.__stdout__

        # Check if the output matches the expected string
        expected_output = '###\n  ###\n  ###\n  ###'
        self.assertEqual(output, expected_output)

    def test_display(self):
        # Create a rectangle object
        rectangle = Rectangle(3, 4, 2, 5)

        # Redirect the stdout to a buffer
        from io import StringIO
        buffer = StringIO()
        import sys
        sys.stdout = buffer

        # Call the display method
        rectangle.display()

        # Get the printed output from the buffer
        output = buffer.getvalue().strip()

        # Reset the stdout
        sys.stdout = sys.__stdout__

        # Check if the output matches the expected string
        expected_output = '###\n  ###\n  ###\n  ###'
        self.assertEqual(output, expected_output)
        

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