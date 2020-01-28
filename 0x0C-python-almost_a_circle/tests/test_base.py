#!/usr/bin/python3
"""
Unit tests for Base class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_Base(unittest.TestCase):
    """Base class tests"""
    def test_validate(self):
        """ validate the id number, without args """
        A1 = Base()
        self.assertEqual(A1.id, 1)
        A2 = Base()
        self.assertEqual(A2.id, 2)
        A3 = Base()
        self.assertEqual(A3.id, 3)

    def test_validate1(self):
        """ validate the id number, with args """
        B1 = Base(25)
        self.assertEqual(B1.id, 25)
        B2 = Base(-13)
        self.assertEqual(B2.id, -13)

    def test_validate2(self):
        """ validate the id number, with 2 or more args"""
        with self.assertRaises(TypeError):
            C1 = Base(3, 7)

    def test_validate3(self):
        """ validate if the args is str """
        D1 = Base("13")
        self.assertEqual(D1.id, "13")

    def test_validate4(self):
        """ validate if the args is str """
        E1 = Base((1, 2))
        self.assertEqual(E1.id, (1, 2))

    def test_validate5(self):
        """ validate if the args is str """
        F1 = Base({"hi": 10, "betty": 20})
        self.assertEqual(F1.id, {"hi": 10, "betty": 20})

    def test_validate6(self):
        """ validate if the args is str """
        G1 = Base([1, 2])
        self.assertEqual(G1.id, [1, 2])

    def test_validate7(self):
        """Validate Dictionary to JSON"""
        H1 = Rectangle(10, 7, 2, 8)
        dictionary = H1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dicts = {'x': 2, 'width': 10, 'id': 4, 'height': 7, 'y': 8}
        lists = '[{"x": 2, "y": 8, "id": 4, "height": 7, "width": 10}]'
        self.assertEqual(dictionary, dicts)
        self.assertEqual(json_dictionary, lists)

    def test_validate8(self):
        """JSON string to dictionary"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        l = [
            {'height': 4, 'width': 10, 'id': 89},
            {'height': 7, 'width': 1, 'id': 7}
        ]
        self.assertEqual(list_output, l)
        self.assertEqual(isinstance(list_output, list), True)

    def test_validate9(self):
        """Dictionary to instance"""
        I1 = Rectangle(3, 5, 1)
        I1_dictionary = I1.to_dictionary()
        I2 = Rectangle.create(**I1_dictionary)
        self.assertEqual(I2.__str__(), "[Rectangle] (5) 1/0 - 3/5")
        self.assertNotEqual(I1, I2)
        self.assertIsNot(I1, I2)


if __name__ == "__main__":
    unittest.main()
