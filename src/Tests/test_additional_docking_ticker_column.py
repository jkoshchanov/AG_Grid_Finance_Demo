#TODO 5. Additional Test:
# Identify and implement at least two more tests that you believe are important to verify for this grid.
# Be prepared to explain your reasoning for choosing these tests.
# For instance: drag the Ticker column after Instrument column and verify undocking/docking is successful
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

# Open the specified URL
driver.get("https://www.ag-grid.com/example-finance/")
print(driver.title)
print(driver.current_url)


# Locate the "Ticker" and "Instrument" column headers using XPath
ticker_column = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@col-id='ticker']")))
instrument_column = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@col-id='instrument']")))

# Perform the drag-and-drop action to move "Ticker" after "Instrument"
actions = ActionChains(driver)
actions.click_and_hold(ticker_column).move_to_element(instrument_column).move_by_offset(50, 0).release().perform()

# Brief pause to allow the grid to update
time.sleep(5)

# Verification
# Check if "Ticker" column is now located after "Instrument" in the header row
# rows = WebDriverWait(driver, 10).until(
#     EC.presence_of_all_elements_located((By.XPATH, "//*[@role='row']")))
header_cells = driver.find_elements(By.XPATH, "//div[@role='columnheader']")
# header_cells = rows[0].text

header_order = [cell.get_attribute("col-id") for cell in header_cells]
print(header_order)

# Verify the "Ticker" column is now positioned after the "Instrument" column
try:
    assert header_order.index("instrument") < header_order.index("ticker"), "Ticker column is not positioned after Instrument column"
    print("Undocking and docking successful: 'Ticker' column is now after 'Instrument'")
except AssertionError as e:
    print(e)

# Close the browser
# driver.quit()

