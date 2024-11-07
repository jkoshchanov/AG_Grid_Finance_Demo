#TODO Assignment 2. Instrument Column Validation:
# Ensure that the cells in the "Instrument" column contain one of the following
# values: Bond | ETF | Crypto | Stock

import unittest
from selenium import webdriver
from Pages.finance_grid_page import FinanceGridPage

expected_values = ["Bond", "ETF", "Crypto", "Stock"]


class InstrumentColumnValidation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.page = FinanceGridPage(self.driver)

    def test_validate_columns(self):
        ticker_texts = self.page.get_all_column_text('ticker')
        instrument_texts = self.page.get_all_column_text('instrument')
        validity, msg = self.page.check_invalid_values(ticker_texts, instrument_texts, expected_values)
        if validity:
            print('cells in the "Instrument" column '
                  'contain one of the following values: '
                  'Bond | ETF | Crypto | Stock')

        self.assertTrue(validity, msg=msg)

    def tearDown(self):
        # Close the browser
        self.driver.quit()


# this helps us to run tests as a suite and better integration with CI/CD
# this also provides clear output for each test indicating pass/fail reasons
if __name__ == '__main__':
    unittest.main()