import unittest
from solverFuncs import *


puzzle = ['WAQHGTTWEE',
          'CBMIVQQELS',
          'APXWKWIIIL',
          'LDELFXPIPV',
          'PONDTMVAMN',
          'OEDSOYQGOB',
          'LGQCKGMMCT',
          'YCSLOACUZM',
          'XVDMGSXCYZ',
          'UUIUNIXFNU']

transpose = transposeWord(puzzle, 10)

class TestCases(unittest.TestCase):  
   def test_search_rows1(self):
      self.assertEqual(search_rows(puzzle, "POND"), (4, 0, 0))

   def test_search_rows2(self):
      self.assertEqual(search_rows(puzzle, "UNIX"), (9, 3, 0))

   def test_search_rows3(self):
      self.assertEqual(search_rows(puzzle, "ari"), (-1, -1, -1))

   def test_search_rows4(self):
      self.assertEqual(search_rows(puzzle, "VIM"), (1, 4, 1))

   def test_search_rows5(self):
      self.assertEqual(search_rows(puzzle, "UNF"), (9, 9, 1))

   def test_search_rows6(self):
      self.assertEqual(search_rows(puzzle, "GKCQ"), (6, 5, 1))

   def test_search_row1(self):
      word = 'UNIX'
      row = 'UUIUNIXFNU'
      self.assertEqual(search_row(row, word), 3)

   def test_search_row2(self):
      word = 'POND'
      row = 'PONDTMVAMN'
      self.assertEqual(search_row(row, word), 0)


   def test_reverseWord1(self):
      word = 'WAQHGTTWEE'
      self.assertEqual(reverseWord(word), 'EEWTTGHQAW')

   def test_reverseWord2(self):
      word = 'UUIUNIXFNU'
      self.assertEqual(reverseWord(word), 'UNFXINUIUU')

   def test_search_cols1(self):
      word = 'CALPOLY'
      self.assertEqual(search_cols(puzzle, word), (1, 0, 2))

   def test_search_cols2(self):
      word = 'ari'
      self.assertEqual(search_cols(puzzle, word), (-1, -1, -1))

   def test_search_cols3(self):
      word = 'COMPILE'
      self.assertEqual(search_cols(puzzle, word), (6, 8, 3))

   def test_transposeWord1(self):
      self.assertEqual(transposeWord(puzzle, 10), transpose)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()