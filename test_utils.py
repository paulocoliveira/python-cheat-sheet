# File: test_utils.py

def take_screenshot(driver, file_name):
    driver.save_screenshot(file_name)
    print(f"Screenshot saved as {file_name}")

def assert_element_present(driver, locator):
    try:
        driver.find_element(*locator)
        print("Element found")
        return True
    except:
        print("Element not found")
        return False