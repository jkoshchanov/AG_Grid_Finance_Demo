#TODO 2. Instrument Column Validation:
# Ensure that the cells in the "Instrument" column contain one of the following values: Bond | ETF | Crypto | Stock


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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
#dictionary for invalid values
invalid_values = {}
# Expected set of values in the "Instrument" column
expected_values = ["Bond", "", "Crypto", "Stock"] # put them in list
# Locate all rows in the grid
rows = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//*[@role='row']")))
ticker_elements = driver.find_elements(By.XPATH, "//*[@col-id='ticker']") #grabbing ticker data as a key
instrument_elements = driver.find_elements(By.XPATH, "//*[@col-id='instrument']")

#loop range
for i in range(len(instrument_elements)): #using range to avoid using sequential loops for efficiency
    if i > 0: #skip header row
        stock = ticker_elements[i].text #assigning value to stock
        instrument = instrument_elements[i].text #assigning value to instrument
        if instrument not in expected_values:
            invalid_values[stock] = instrument


if len(invalid_values) > 0:
    print('something is wrong, check the following stock names: ' + ", ".join(invalid_values.keys()))

else:
    print('looks good')

# Close the browser
driver.quit()
