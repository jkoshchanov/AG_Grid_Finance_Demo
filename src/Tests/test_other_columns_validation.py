#TODO 3. Numeric Columns Validation:
# Confirm that the cells in the following columns contain numeric values: P&L | Total Value | Quantity | Price

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# Open the specified URL
driver.get("https://www.ag-grid.com/example-finance/")
print(driver.title)
print(driver.current_url)

# Dict of column IDs to verify for numeric values, using key-value pair
numeric_columns = {"0": 'P&L',
                   "1": 'Total Value',
                   "quantity": "Quantity",
                   "purchasePrice": "Price"}


# Function to check if a value is numeric
def is_numeric(value):
    if value == '' or value is None:
        return False
    try: #letting the program to continue despite raising an error
        float(value.replace(',', ''))  # Try converting to float
        return True
    except ValueError:
        return False

# Flag to check if all cells in numeric columns are valid
all_cells_valid = True #by default

# HTML: P%L and Total (fluctuating changes)
# 1,082.41
# HTML of Quantity and Price (fixed)
# 1,000

# Loop over each column and validate numeric cells
for column_id, column_name in numeric_columns.items():
    # Locate all rows in the grid
    rows = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//*[@role='row']")))

    # Iterate over each row to find the cell in the current column
    for row in rows[1:]:
        # Find the cell in the current column using XPath
        cell = driver.find_element(By.XPATH, f"//div[@role='gridcell' and @col-id='{column_id}']")
        cell_value = cell.find_element(By.CLASS_NAME, "ag-value-change-value").text if column_id in ["0", "1"] else cell.text
        # print(f"Value in {column_name} is {cell_value}")

        # For testing only
        # cell_value = "test"

        # Check if the cell's text is numeric
        if not is_numeric(cell_value):
            print(f"Non-numeric value found in column '{column_name}': {cell_value}")
            all_cells_valid = False
        # else:
        #     print(f"Numeric value in column '{column_name}': {cell_value}")

# Final assertion to validate that all cells are numeric
assert all_cells_valid, "Not all cells in specified columns contain numeric values."
print('Test execution is completed, confirmed the cells have numeric values')

# Close the browser
driver.quit()

