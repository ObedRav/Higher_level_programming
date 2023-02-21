import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def setUp(self):
        # Reset the Base class' _Base__nb_objects attribute before each test
        Base._Base__nb_objects = 0

    def test_init(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        r1_dict = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        r2_dict = {'id': 2, 'width': 2, 'height': 4, 'x': 0, 'y': 0}
        r1_json = Base.to_json_string([r1_dict])
        r2_json = Base.to_json_string([r2_dict])
        self.assertEqual(r1_json, json.dumps([r1_dict]))
        self.assertEqual(r2_json, json.dumps([r2_dict]))

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}, {"x": 0, "y": 0, "id": 2, "height": 4, "width": 2}]')


if __name__ == '__main__':
    unittest.main()
