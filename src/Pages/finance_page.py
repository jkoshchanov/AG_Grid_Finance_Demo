class FinancePage():
    def __init__(self, driver):
        self.driver = driver

        self.ticker_column_header = "//div[@col-id='ticker']"
        self.instrument_column_header = "//div[@col-id='instrument']"
        self.pl_column_header = ""

