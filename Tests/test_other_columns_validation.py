#TODO Assignment 3. Numeric Columns Validation:
# Confirm that the cells in the following columns contain numeric
# values: P&L | Total Value | Quantity | Price

import unittest
from selenium import webdriver
from finance_grid_page import FinanceGridPage

numeric_columns = {"0": 'P&L',
                   "1": 'Total Value',
                   "quantity": "Quantity",
                   "purchasePrice": "Price"}

class TestNumericColumnValidation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.page = FinanceGridPage(self.driver)

    def test_validate_numeric_columns(self):
       self.assertTrue(self.page.is_all_cells_valid(numeric_columns))

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()