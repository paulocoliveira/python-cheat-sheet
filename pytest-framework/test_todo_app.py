import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    username = os.getenv("LT_USERNAME")
    accessToken = os.getenv("LT_ACCESS_KEY")
    gridUrl = "hub.lambdatest.com/wd/hub"

    options = webdriver.ChromeOptions()
    options.browser_version = "latest"
    options.platform_name = "Windows 11"
    lt_options = {}
    lt_options["username"] = username
    lt_options["accessKey"] = accessToken
    lt_options["build"] = "your build name"
    lt_options["project"] = "your project name"
    lt_options["name"] = "your test name"
    options.set_capability('LT:Options', lt_options)
    
    url = "https://"+username+":"+accessToken+"@"+gridUrl
    
    driver = webdriver.Remote(
        command_executor=url,
        options=options
    )

    yield driver
    
    driver.quit

# Test function to verify the Todo App functionality
def test_todo_app(driver):
    driver.get("https://lambdatest.github.io/sample-todo-app/")
    driver.maximize_window()

    checkbox = driver.find_element(By.NAME, "li1")
    checkbox.click()
    assert checkbox.is_selected()

    text_field = driver.find_element(By.ID, "sampletodotext")
    text_field.send_keys("New Item")

    add_button = driver.find_element(By.ID, "addbutton")
    add_button.click()

    todos = driver.find_elements(By.CSS_SELECTOR, "ul.list-unstyled li")
    assert len(todos) == 6