#TODO 2. Instrument Column Validation:
# Ensure that the cells in the "Instrument" column contain one of the following values: Bond | ETF | Crypto | Stock

import unittest
from selenium import webdriver
from finance_grid_page import FinanceGridPage

expected_values = ["Bond", "ETF", "Crypto", "Stock"]


class InstrumentColumnValidation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.page = FinanceGridPage(self.driver)

    def test_validate_columns(self):

        instruments = self.page.get_column_text("instrument")
        ticker_elements = self.page.get_column_text("ticker")
        invalid_values = self.page.get_invalid_values(instruments, ticker_elements, expected_values)
        self.assertTrue(self.page.verify_no_invalid_values(invalid_values))

    def tearDown(self):
        # Close the browser
        self.driver.quit()


# this helps us to run tests as a suite and better integration with CI/CD
# this also provides clear output for each tests indicating pass/fail reasons
if __name__ == '__main__':
    unittest.main()