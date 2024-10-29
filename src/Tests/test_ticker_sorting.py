#TODO 1. Create an automated end-to-end test suite for the "Finance" demo grid available at: https://www.ag-grid.com/example-finance/
# Your test suite should verify the Sorting Functionality
# Verify that the grid can be sorted by the "Ticker" column

from selenium import webdriver
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

# Locate the "Ticker" column header
ticker_header = driver.find_element(By.XPATH, "//div[@col-id='ticker']")

def get_all_rows():
    rows = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*[@role='row']"))
            )

    ticker_elements = driver.find_elements(By.XPATH, "//*[@col-id='ticker']")
    ticker_text = [element.text
                   for element in ticker_elements
                   if element.text][1:]
    print(ticker_text)
    print(len(ticker_text))

    return ticker_text[1:]


# double click for descending
ticker_header.click() # on first click, not getting ascending order as expected
time.sleep(5)  # Small delay to allow the sort to apply
ticker_header.click()
time.sleep(5)  # Small delay to allow the sort to apply

ticker_text = get_all_rows()
sorted_ticker_text = sorted(ticker_text, reverse=True) # sorting for DESC order
print(sorted_ticker_text)

assert sorted_ticker_text == ticker_text

print("Test passed: Ticker column is sorted correctly")
# Close the browser
driver.quit()
