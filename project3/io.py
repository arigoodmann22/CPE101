import unittest
from solverFuncs import *


puzzleList = ['WAQHGTTWEE',
          'CBMIVQQELS',
          'APXWKWIIIL',
          'LDELFXPIPV',
          'PONDTMVAMN',
          'OEDSOYQGOB',
          'LGQCKGMMCT',
          'YCSLOACUZM',
          'XVDMGSXCYZ',
          'UUIUNIXFNU']

wordList = ['UNIX', 'CALPOLY', 'SLO', 'COMPILE', 'VIM', 'TEST']


class TestCases(unittest.TestCase):   
   # This test requires you to pass in an input file
   # The unit test checks you stored the values properly
   # You can diff the output also
   def test_read_puzzle(self): #given
      self.assertEqual(read_puzzle(), puzzleList) #given

   def test_read_words(self):
      self.assertEqual(read_words(), wordList)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()