from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

@given('I open the Todo App page')
def open_todo_app_page(context):
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
    
    context.driver = webdriver.Remote(
        command_executor=url,
        options=options
    )

    context.driver.get("https://lambdatest.github.io/sample-todo-app/")
    context.driver.maximize_window()

@when('I check the first todo')
def check_first_todo_checked(context):
    checkbox = context.driver.find_element(By.NAME, "li1")
    checkbox.click()

@then('it should be marked as done')
def check_first_todo_done(context):
    checkbox = context.driver.find_element(By.NAME, "li1")
    assert checkbox.is_selected()

@then('a new todo can be added')
def add_new_todo(context):
    text_field = context.driver.find_element(By.ID, "sampletodotext")
    text_field.send_keys("New Item")
    add_button = context.driver.find_element(By.ID, "addbutton")
    add_button.click()

@then('the total number of todos should be {count:d}')
def check_total_todos_count(context, count):
    todos = context.driver.find_elements(By.CSS_SELECTOR, "ul.list-unstyled li")
    assert len(todos) == count

@then('the browser should be closed')
def close_browser(context):
    context.driver.quit()