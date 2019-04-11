import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        # tests for list of value None
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

        # test for list of all positive numbers
        list1 = [1,2,3]
        self.assertEqual(max_list_iter(list1), 3)

        #tests for list with negative values
        list2 = [-1,0,-5]
        self.assertEqual(max_list_iter(list2), 0)

        #tests for empty list
        list3 = []
        self.assertEqual(max_list_iter(list3), 'None')

    def test_reverse_rec(self):
        #tests for list of positive values in order
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        #tests for list with positive values out of order
        self.assertEqual(reverse_rec([5,2,7]),[7,2,5])
        #tests for list with value 0
        self.assertEqual(reverse_rec([0,2,3,5]),[5,3,2,0])
        #tests for list with all negative values
        self.assertEqual(reverse_rec([-1,2,-3,-5]),[-5,-3,2,-1])
        #tests for list with decimal values
        self.assertEqual(reverse_rec([1.4,2.8,6,9]),[9,6,2.8,1.4])
        # tests for empty list
        self.assertEqual(reverse_rec([]),[])
        #tests for list of value None
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_bin_search(self):
        # tests for target in middle of list
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

        #tests for target on left
        list_val2 =[3,6,9,12,15]
        low2 = 0
        high2 = len(list_val2)-1
        self.assertEqual(bin_search(3, 0, len(list_val2)-1, list_val2), 0 )

        #tests for target on right
        list_val3 =[2,4,6,8,10,12,14]
        low3 = 0
        high3 = len(list_val3)-1
        self.assertEqual(bin_search(12, 0, len(list_val3)-1, list_val3), 5 )

        #tests for value out of range on right
        list_val4 =[2,2,4,5,6,7,7,8]
        low4 = 2
        high4 = 4
        self.assertEqual(bin_search(7, 0, 4, list_val4), None)

        #tests for value out of range on left
        list_val5 =[2,2,4,5,6,7,7,8]
        low5 = 3
        high5 = 7
        self.assertEqual(bin_search(4, 3, 7, list_val5), None)

        #tests for empty list
        list_val6 =[]
        low6 = 0
        high6 = 7
        self.assertEqual(bin_search(4, 0, 7, list_val6), None)

        #tests for list of value None
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(4,0,7,tlist)

        # tests for list of length 1
        list_val7 =[4]
        low7 = 0
        high7 = len(list_val7)-1
        self.assertEqual(bin_search(4, 0, len(list_val7)-1, list_val7), 0)

        # tests for negative value out of range
        list_val8 =[-3, 0, 5.1, 12]
        low8 = 0
        high8 = len(list_val8)-1
        self.assertEqual(bin_search(-3, 2, len(list_val8)-1, list_val8), None)

        #tests for value not included in list
        list_val9 =[-3, 0, 5.1, 12]
        low9 = 0
        high9 = len(list_val9)-1
        self.assertEqual(bin_search(4, 0, len(list_val9)-1, list_val9), None)

if __name__ == "__main__":
        unittest.main()
