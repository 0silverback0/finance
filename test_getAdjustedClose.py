import unittest
from getAdjustedClose import getAdjustedClose

class TestGetAdjustedClose(unittest.TestCase):
    def test_getAdjustedClose(self):
        """ test if first element is there and capitalized """

        tickers = ['dnp', 'tsla', 'o', 'gof']
        data = getAdjustedClose(tickers)
        self.assertEqual(data.columns[0], 'DNP')