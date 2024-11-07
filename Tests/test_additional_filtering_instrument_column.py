#TODO Assignment 4. Additional Test:
# Identify and implement at least two more tests that you believe are important to verify for this grid.
# Be prepared to explain your reasoning for choosing these tests.
# For instance: filter Instrument column by Bond, Crypto, ETF, Stock
# and return the number of rows for each filter in an array or list

import unittest
from selenium import webdriver
from finance_grid_page import FinanceGridPage

instrument_filters = ["Bond", "Crypto", "ETF", "Stock"]

class TestSearchAndFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.page = FinanceGridPage(self.driver)

    def test_search_and_filter(self):
       self.page.search_and_filter(instrument_filters)

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()