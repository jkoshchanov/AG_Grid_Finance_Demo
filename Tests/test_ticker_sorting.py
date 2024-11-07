#TODO 1. Create an automated end-to-end test suite for the "Finance" demo grid available at: https://www.ag-grid.com/example-finance/
# Your test suite should verify the Sorting Functionality
# Verify that the grid can be sorted by the "Ticker" column

import unittest
from selenium import webdriver
from finance_grid_page import FinanceGridPage


class TestTickerSorting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.page = FinanceGridPage(self.driver)

    def test_sort_ticker_column_descending(self):
        self.page.sort_ticker_column_descending()
        ticker_texts = self.page.get_column_text('ticker')
        self.assertTrue(self.page.is_sorted_descending(ticker_texts))

    def tearDown(self):
        # Close the browser
        self.driver.quit()


# this helps us to run tests as a suite and better integration with CI/CD
# this also provides clear output for each tests indicating pass/fail reasons
if __name__ == '__main__':
    unittest.main()