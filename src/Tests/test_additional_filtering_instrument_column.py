#TODO 4. Additional Test:
# Identify and implement at least two more tests that you believe are important to verify for this grid.
# Be prepared to explain your reasoning for choosing these tests.
# For instance: filter Instrument column by Bond, Crypto, ETF, Stock
# and return the number of rows for each filter in an array or list

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# Open the specified URL
driver.get("https://www.ag-grid.com/example-finance/")
print(driver.title)
print(driver.current_url)

# List of filter values for the "Instrument" column
instrument_filters = ["Bond", "Crypto", "ETF", "Stock"]

# Dictionary to store the number of rows for each filter
row_counts = {}


# Function to apply a filter and return the row count
def apply_filter_and_count_rows(instrument_type):
    # Open the filter menu for the "Instrument" column
#<div class="ag-header-cell-comp-wrapper" role="presentation"><div class="ag-cell-label-container" role="presentation">
#     <span data-ref="eMenu" class="ag-header-icon ag-header-cell-menu-button ag-header-menu-icon ag-header-menu-always-show" aria-hidden="true"><span class="ag-icon ag-icon-menu-alt" unselectable="on" role="presentation"></span></span>
#     <span data-ref="eFilterButton" class="ag-header-icon ag-header-cell-filter-button ag-has-popup-positioned-under" aria-hidden="true"><span class="ag-icon ag-icon-filter" unselectable="on" role="presentation"></span></span>
#     <div data-ref="eLabel" class="ag-header-cell-label" role="presentation">
#         <span data-ref="eText" class="ag-header-cell-text">Instrument</span>
#
#<div role="presentation" class="ag-mini-filter ag-labeled ag-label-align-left ag-text-field ag-input-field" data-ref="eMiniFilter">
#     <div data-ref="eLabel" class="ag-input-field-label ag-label ag-hidden ag-text-field-label" aria-hidden="true" role="presentation" id="ag-114-label"></div>
#     <div data-ref="eWrapper" class="ag-wrapper ag-input-wrapper ag-text-field-input-wrapper" role="presentation">
#         <input data-ref="eInput" class="ag-input-field-input ag-text-field-input" type="text" id="ag-114-input" tabindex="0" aria-label="Search filter values" placeholder="Search..." control-id="ControlID-4">
#     </div>
# </div>
    instrument_filter_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@col-id='instrument']//span[@data-ref='eFilterButton']"))
    )
    # print("Instrument button", instrument_filter_button)
    instrument_filter_button.click()

    # Locate the filter input, clear it, and enter the instrument type
    filter_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@data-ref='eMiniFilter']//input[@data-ref='eInput']"))
    )
    # print("Filter input", filter_input)
    filter_input.clear()
    filter_input.send_keys(instrument_type)
    filter_input.send_keys(Keys.RETURN)


    # Allow some time for the grid to refresh with the filtered rows
    time.sleep(2)

    # Get all rows displayed after filtering
    rows = driver.find_elements(By.XPATH, "//div[contains(@class, 'ag-row')]")

    # Close the filter menu by clicking elsewhere (outside the menu)
    driver.find_element(By.XPATH, "//body").click()

    # Return the row count
    return len(rows)


# # Apply each filter and store the row count
for instrument in instrument_filters:
    row_count = apply_filter_and_count_rows(instrument)
    row_counts[instrument] = row_count
    print(f"Rows for '{instrument}': {row_count}")

# Close the browser
driver.quit()