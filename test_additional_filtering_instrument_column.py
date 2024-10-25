#TODO 4. Additional Test:
# Identify and implement at least two more tests that you believe are important to verify for this grid.
# Be prepared to explain your reasoning for choosing these tests.
# For instance: filter Instrument column by Bond, Crypto, ETF, Stock
# and return the number of rows for each filter in an array or list

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

# List of filter values for the "Instrument" column
instrument_filters = ["Bond", "Crypto", "ETF", "Stock"]

# Dictionary to store the number of rows for each filter
row_counts = {}


# Function to apply a filter and return the row count
def apply_filter_and_count_rows(instrument_type):
    # Open the filter menu for the "Instrument" column
    instrument_filter_button = driver.find_element(By.XPATH, "//div[@col-id='instrument']//span[@ref='eMenu']")
    instrument_filter_button.click()

    # Wait for the filter input to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//input[@placeholder='Filter...']")))

    # Locate the filter input, clear it, and enter the instrument type
    filter_input = driver.find_element(By.XPATH, "//div[@role='dialog']//input[@placeholder='Filter...']")
    filter_input.clear()
    filter_input.send_keys(instrument_type)

    # Allow some time for the grid to refresh with the filtered rows
    time.sleep(2)

    # Get all rows displayed after filtering
    rows = driver.find_elements(By.XPATH, "//div[contains(@class, 'ag-row')]")

    # Close the filter menu by clicking elsewhere (outside the menu)
    driver.find_element(By.XPATH, "//body").click()

    # Return the row count
    return len(rows)


# Apply each filter and store the row count
for instrument in instrument_filters:
    row_count = apply_filter_and_count_rows(instrument)
    row_counts[instrument] = row_count
    print(f"Rows for '{instrument}': {row_count}")

# Close the browser
driver.quit()

# Output row counts as a list
row_count_list = list(row_counts.values())
print("Row counts for each instrument type:", row_count_list)
