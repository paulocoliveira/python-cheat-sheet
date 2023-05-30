from lettuce import step, world
from selenium import webdriver

@step('I open the Todo App page')
def open_todo_app_page(step):
    world.driver = webdriver.Chrome()

@step('the title should be "(.*?)"')
def check_title(step, title):
    assert world.driver.title == title

@step('there should be (\d+) todos displayed')
def check_todos_count(step, count):
    todos = world.driver.find_elements_by_css_selector("ul.list-unstyled li")
    assert len(todos) == int(count)

@step('the first todo should be unchecked')
def check_first_todo_unchecked(step):
    checkbox = world.driver.find_element_by_name("li1")
    assert not checkbox.is_selected()

@step('I check the first todo')
def check_first_todo_checked(step):
    checkbox = world.driver.find_element_by_name("li1")
    checkbox.click()

@step('it should be marked as done')
def check_first_todo_done(step):
    checkbox = world.driver.find_element_by_name("li1")
    assert checkbox.is_selected()
    assert world.driver.find_element_by_css_selector("span.done-true").is_displayed()

@step('a new todo can be added')
def add_new_todo(step):
    add_button = world.driver.find_element_by_id("addbutton")
    add_button.click()
    todos = world.driver.find_elements_by_css_selector("ul.list-unstyled li")
    assert len(todos) == 6

@step('the total number of todos should be (\d+)')
def check_total_todos_count(step, count):
    todos = world.driver.find_elements_by_css_selector("ul.list-unstyled li")
    assert len(todos) == int(count)

@step('the browser should be closed')
def close_browser(step):
    world.driver.quit()