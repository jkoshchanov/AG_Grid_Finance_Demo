#TODO Assignment 5. Additional Test:
# Identify and implement at least two more tests that you believe are important to verify for this grid.
# Be prepared to explain your reasoning for choosing these tests.
# For instance: drag the Ticker column after Instrument column and verify undocking/docking is successful

import unittest
from selenium import webdriver
from Pages.finance_grid_page import FinanceGridPage

class TestSearchAndFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.page = FinanceGridPage(self.driver)

    def test_grid_column_position_change(self):
        ticker_column = self.page.retrieve_column(self.page.TICKER_HEADER)
        instrument_column = self.page.retrieve_column(self.page.INSTRUMENTS_HEADER)

        # retrieving positions of the columns before drag-drop
        ticker_x_position1 = self.page.retrieve_x_position(ticker_column)
        instrument_x_position1 = self.page.retrieve_x_position(instrument_column)

        # using drag-drop the ticker column after instrument column
        self.page.drag_drop(ticker_column, instrument_column)

        # retrieving positions of the column after drag-drop
        ticker_x_position2 = self.page.retrieve_x_position(ticker_column)
        instrument_x_position2 = self.page.retrieve_x_position(instrument_column)

        # validation of the changed column position
        assert ticker_x_position1 < ticker_x_position2
        assert instrument_x_position1 > instrument_x_position2
        assert ticker_x_position1 < instrument_x_position1
        assert ticker_x_position2 > instrument_x_position2

        print("Undocking and docking successful: 'Ticker' column is now after 'Instrument'")

    def tearDown(self):
        # Close the browser
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()