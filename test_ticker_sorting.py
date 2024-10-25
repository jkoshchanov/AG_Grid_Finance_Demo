#TODO 1. Create an automated end-to-end test suite for the "Finance" demo grid available at: https://www.ag-grid.com/example-finance/
# Your test suite should verify the Sorting Functionality
# Verify that the grid can be sorted by the "Ticker" column

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver
# Chrome driver - Chrome browser
    # --Chrome
service_obj = Service()  # seleniumManager
# set up chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# initialize the webdriver
driver = webdriver.Chrome(options=options, service=service_obj)
# add global timeout for 10 seconds max
driver.implicitly_wait(10)

# Open the specified URL
driver.get("https://www.ag-grid.com/example-finance/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)


# Locate the "Ticker" column header
ticker_header = driver.find_element(By.XPATH, "//div[@col-id='ticker']")


# Function to get the first and last Ticker values in the grid
def get_first_last_ticker_values():
    # Wait for rows to be present
    rows = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.ag-row')))

    # Get the first and last rows' Ticker cell values
    first_row_value = rows[0].find_element(By.XPATH, ".//div[@col-id='ticker']").text
    print(first_row_value)
    last_row_value = rows[-1].find_element(By.XPATH, ".//div[@col-id='ticker']").text
    print(last_row_value)

    return first_row_value, last_row_value


# Click once to sort Ticker column in one direction
ticker_header.click()
time.sleep(2)  # Small delay to allow the sort to apply
first_sort = first_sort_first_row, first_sort_last_row = get_first_last_ticker_values()
print(first_sort)
print(get_first_last_ticker_values())

# Click again to sort Ticker column in the other direction
ticker_header.click()
time.sleep(2)  # Small delay to allow the sort to apply
second_sort = second_sort_first_row, second_sort_last_row = get_first_last_ticker_values()
print(second_sort)
print(get_first_last_ticker_values())

# Validate if the first and last rows have been swapped after sorting
is_valid_sort = (first_sort_first_row == second_sort_last_row) and (first_sort_last_row == second_sort_first_row)
assert first_sort_first_row == second_sort_last_row, "First row after first sort does not match last row after second sort"
assert first_sort_last_row == second_sort_first_row, "Last row after first sort does not match first row after second sort"

# Output the results
print("First Sort - First Row:", first_sort_first_row)
print("First Sort - Last Row:", first_sort_last_row)
print("Second Sort - First Row:", second_sort_first_row)
print("Second Sort - Last Row:", second_sort_last_row)
print("Sorting Validated:", is_valid_sort)

# Close the browser
driver.quit()