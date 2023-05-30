from selenium import webdriver
from test_utils import take_screenshot, assert_element_present

# Create a webdriver instance
driver = webdriver.Chrome()

# Use the utilities from the test_utils module
take_screenshot(driver, "homepage.png")

locator = ("id", "login_button")
assert_element_present(driver, locator)

# Close the webdriver instance
driver.quit()