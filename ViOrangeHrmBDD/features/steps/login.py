'''
Created on 25-Jun-2026

@author: Vivek
'''
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'Chrome browser is launched')
def step_launch_chrome_browser(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("start-maximized")
    
    context.driver = webdriver.Chrome(options)
    context.driver.implicitly_wait(10)


@when(u'User navigates to Login Page URL')
def step_navigate_orangehrm_login_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@then(u'User should see login in current page URL')
def step_validate_login_page(context):
    current_page_url = context.driver.current_url
    print(context.driver.current_url)
    assert "login" in current_page_url, "Navigation Failed"
