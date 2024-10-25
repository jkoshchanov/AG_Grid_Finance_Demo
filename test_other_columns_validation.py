#TODO 3. Numeric Columns Validation:
# Confirm that the cells in the following columns contain numeric values: P&L | Total Value | Quantity | Price

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

# List of column IDs to verify for numeric values
numeric_columns = [0, 1, "quantity", "purchasePrice"]


# Function to check if a value is numeric
def is_numeric(value):
    if value == '' or value is None:
        return False
    try:
        float(value.replace(',', ''))  # Try converting to float
        return True
    except ValueError:
        return False


# Flag to check if all cells in numeric columns are valid
all_cells_valid = True

# Loop over each column and validate numeric cells
for column_id in numeric_columns:
    # Locate all rows in the grid
    rows = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'ag-row')]")))

    # Iterate over each row to find the cell in the current column
    for row in rows:
        # Find the cell in the current column using XPath
        cell = row.find_element(By.XPATH, f".//div[@col-id='{column_id}']")
        cell_value = cell.text
        print(cell_value)

        # Check if the cell's text is numeric
        if not is_numeric(cell_value):
            print(f"Non-numeric value found in column '{column_id}': {cell_value}")
            all_cells_valid = False
        else:
            print(f"Numeric value in column '{column_id}': {cell_value}")

# Final assertion to validate that all cells are numeric
assert all_cells_valid, "Not all cells in specified columns contain numeric values."

# Close the browser
driver.quit()
