import unittest
import os
from service.src.utility.PropertyReader import PropertyReader


class TestPropertyReader(unittest.TestCase):
    def setUp(self):
        self.filename = "text.ini"
        try:
            with open(self.filename, 'w') as f:
                f.write("key=value")
        except IOError:
            print("Error create file")

    def test_read_property_and_return_value_by_key(self):
        pr = PropertyReader(self.filename)
        self.assertEqual(pr.get("key"), "value")

    def tearDown(self):
        os.remove(self.filename)
