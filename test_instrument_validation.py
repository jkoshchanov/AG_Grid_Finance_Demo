#TODO 2. Instrument Column Validation:
# Ensure that the cells in the "Instrument" column contain one of the following values: Bond | ETF | Crypto | Stock


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# Expected set of values in the "Instrument" column
expected_values = {"Bond", "ETF", "Crypto", "Stock"}

# Locate all rows in the grid
rows = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'ag-row')]")))

# Verify each cell in the "Instrument" column contains one of the expected values
all_cells_valid = True  # Flag to check if all cells meet the condition

for row in rows:
    # Find the "Instrument" cell in the current row using XPath
    instrument_cell = row.find_element(By.XPATH, ".//div[@col-id='instrument']")
    instrument_value = instrument_cell.text
    print(instrument_value)

    # Check if the cell's text is in the expected values
    if instrument_value not in expected_values:
        print(f"Invalid value found: {instrument_value}")
        all_cells_valid = False
    else:
        print(f"Valid value: {instrument_value}")

# Final assertion to validate that all cells are correct
assert all_cells_valid, "Not all 'Instrument' cells contain valid values."

# Close the browser
driver.quit()
