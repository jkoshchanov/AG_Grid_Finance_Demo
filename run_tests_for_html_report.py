
import os
import unittest
from HtmlTestRunner import HTMLTestRunner


# Ensure the tests directory exists
if not os.path.exists('Tests'):
    raise FileNotFoundError("The 'tests' directory does not exist. Please create it and add test files.")

# Define a test suite by discovering all test cases in the tests folder
loader = unittest.TestLoader()
suite = loader.discover('Tests')  # Assumes tests are in the 'tests' directory

# Run all tests and generate an HTML report
if __name__ == "__main__":
    runner = HTMLTestRunner(output='reports', report_name="Test_Report")
    runner.run(suite)