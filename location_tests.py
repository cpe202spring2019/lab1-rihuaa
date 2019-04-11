import unittest
from location import *

class TestLab1(unittest.TestCase):

    #tests repr function
    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

        loc = Location('Paris', 48.9, 2.4)
        self.assertEqual(repr(loc),"Location('Paris', 48.9, 2.4)")

    #tests equal function
    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location('Paris', 48.9, 2.4)
        self.assertFalse(loc1 == loc2)

        loc3 = Location("SLO", 35.3, -120.7)
        loc4 = Location("SLO", 35.3, -120.7)
        self.assertTrue(loc3 == loc4)

    #tests init function
    def test_init(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc.name, "SLO")
        self.assertEqual(loc.lat, 35.3)
        self.assertEqual(loc.lon, -120.7)


if __name__ == "__main__":
        unittest.main()
