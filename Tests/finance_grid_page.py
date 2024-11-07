from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class FinanceGridPage:
    URL = "https://www.ag-grid.com/example-finance/"

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.URL)
        self.wait = WebDriverWait(self.driver, 10)

    # Locators
    TICKER_HEADER = (By.XPATH, "//div[@col-id='ticker']")
    ROW_LOCATOR = (By.XPATH, "//*[@role='row']")
    INSTRUMENTS_HEADER = (By.XPATH, "//*[@col-id='instrument']")
    INSTRUMENT_FILTER_BUTTON = (By.XPATH, "//div[@col-id='instrument']//span[@data-ref='eFilterButton']")
    FILTER_INPUT = (By.XPATH, "//div[@data-ref='eMiniFilter']//input[@data-ref='eInput']")
    COLUMN_HEADER = (By.XPATH, "//div[@role='columnheader']")
    FILTERED_ROWS =  (By.XPATH, "//div[contains(@class, 'ag-row')]")


    def wait_for_element_visibility(self, locator, timeout=2):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_presence(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def wait_for_cell_presence(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click_element(self, element):
        element.click()
        time.sleep(3)

    def get_column_text(self, column_id):
        self.wait_for_element_presence(self.ROW_LOCATOR)
        column_cells = self.driver.find_elements(By.XPATH, f"//*[@col-id='{column_id}']")
        return [cell.text for cell in column_cells if cell.text][1:]

    # Assignment 1
    def sort_ticker_column_descending(self):
        ticker_header = self.wait_for_element_clickable(self.TICKER_HEADER)
        ticker_header.click()
        ticker_header.click()
        sleep(3)

    def is_sorted_descending(self, column_texts):
        return column_texts == sorted(column_texts, reverse=True)

    # Assignment 2
    def check_invalid_values(self, ticker_texts, instrument_texts, expected_values):
        invalid_values = {}
        for i in range(len(instrument_texts)):  # using range to avoid using sequential loops for efficiency
            if i > 0:  # skip header row
                stock = ticker_texts[i]  # assigning value to stock
                instrument = instrument_texts[i]  # assigning value to instrument
                if instrument not in expected_values:
                    invalid_values[stock] = instrument

        if len(invalid_values) > 0:
            return [False, 'something is wrong, check the following stock names: ' + ", ".join(invalid_values.keys())]
        else:
            return [True, None]

    # Assignment 3
    def get_cell_value(self, row_index, column_id):
        if column_id in ["0", "1"]:
            cell_value = self.driver.find_element(
                By.XPATH,
                f".//div[@role='row' and @row-index='{row_index}']//div[@role='gridcell' and @col-id='{column_id}']//span[@class='ag-value-change-value']"
            ).text
        else:
            cell_value = self.driver.find_element(
                By.XPATH,
                f".//div[@role='row' and @row-index='{row_index}']//div[@role='gridcell' and @col-id='{column_id}']"
            ).text
        return cell_value

    def is_numeric(self, value):
        if value == '' or value is None:
            return False
        try:
            float(value.replace(',', ''))  # Try converting to float
            return True
        except ValueError:
            return False

    def is_all_cells_valid(self, numeric_columns):
        all_cells_valid = True

        # Locate all rows in the grid
        rows = self.wait_for_element_presence(self.ROW_LOCATOR)

        # Loop over each column and validate numeric cells
        for column_id, column_name in numeric_columns.items():
            # Iterate over each row to find the cell in the current column
            for row_index in range(len(rows)-1):
                try:
                    cell_value = self.get_cell_value(row_index, column_id)
                    # Check if the cell's text is numeric
                    if not self.is_numeric(cell_value):
                        print(f"Non-numeric value found in column '{column_name}': {cell_value}")
                        all_cells_valid = False
                except NoSuchElementException:
                    print(f"No more rows found with aria-rowindex '{row_index}'. Exiting loop.")
                    continue

        return all_cells_valid

    # Assignment 4
    def apply_filter_and_count_rows(self, instrument_type):
        instrument_filter_button = self.wait_for_element_clickable(self.INSTRUMENT_FILTER_BUTTON)
        self.click_element(instrument_filter_button)

        # Locate the filter input, clear it, and enter the instrument type
        filter_input = self.wait_for_element_visibility(self.FILTER_INPUT)
        filter_input.clear()
        filter_input.send_keys(instrument_type)
        filter_input.send_keys(Keys.RETURN)

        # Allow some time for the grid to refresh with the filtered rows
        time.sleep(2)

        filtered_rows = self.wait_for_element_presence(self.FILTERED_ROWS)

        self.driver.find_element(By.XPATH, "//body").click()

        return len(filtered_rows)

    def search_and_filter(self, instrument_filters):
        row_counts = {}
        for instrument in instrument_filters:
            row_count = self.apply_filter_and_count_rows(instrument)
            row_counts[instrument] = row_count
            print(f"Rows for '{instrument}': {row_count}")
        return row_counts

    # Assignment 5
    def drag_drop(self, column1, column2):
        actions = ActionChains(self.driver)
        actions.click_and_hold(column1).move_to_element(column2).move_by_offset(50,0).release().perform()
        time.sleep(2)

    def retrieve_column(self, locator):
        return self.wait_for_cell_presence(locator)

    def retrieve_x_position(self, column):
        return column.location['x']




