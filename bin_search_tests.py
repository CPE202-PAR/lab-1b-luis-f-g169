import unittest
from bin_search import *
from typing import List

class TestLab1b(unittest.TestCase):

    def test_bin_search_iter_01(self) -> None:
        tlist: List = [5, 9, 18, 23, 55, 72]
        self.assertEqual(bin_search_iter(tlist, 5), 0)
    #The bug in the program was that the while loop didnt have a equal to so it would not consider when the low was equal to high
    def test_bin_search_iter_03(self) -> None:
        plist: List = [5,8,9,10]
        self.assertEqual(bin_search_iter(plist, 10), 3)

    def test_bin_search_iter_02(self) -> None:
        tlist = None
        with self.assertRaises(ValueError):  # uses context manager for checking exception
            bin_search_iter(tlist, 5)
    
    def test_bin_search_iter_04(self) -> None:
        tlist: List = [1, 2, 3, 4, 5, 6]
        self.assertEqual(bin_search_iter(tlist, 10), None)

    def test_bin_searcg_rec(self) -> None:
         tlist = None
         with self.assertRaises(ValueError):
              bin_search_rec(tlist, 5)
    
    def test_bin_searcg_rec02(self) -> None:
         tlist: List = [5, 9, 18, 23, 55, 72]
         self.assertEqual(bin_search_rec(tlist, 5), 0)

    def test_bin_searcg_rec03(self) -> None:
         tlist: List = [5, 9, 18, 23]
         self.assertEqual(bin_search_rec(tlist, 23), 3)
    

if __name__ == "__main__":
        unittest.main()
