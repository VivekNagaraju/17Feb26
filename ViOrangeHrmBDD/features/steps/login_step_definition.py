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
    context.wait = WebDriverWait(context.driver, timeout=10)


@when(u'User navigates to Login Page URL')
def step_navigate_orangehrm_login_page(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@then(u'User should see login in current page URL')
def step_validate_login_page_url(context):
    current_page_url = context.driver.current_url
    print(context.driver.current_url)
    assert "login" in current_page_url, "Navigation Failed"
    
@when(u'User enters username')
def step_enter_username(context):
    username_textbox = context.wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
    username_textbox.send_keys("Admin")


@when(u'User enters password')
def step_enter_password(context):
    password_textbox = context.wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
    password_textbox.send_keys("admin123")


@when(u'User clicks on login button')
def step_click_login_button(context):
    login_button = context.driver.find_element(By.TAG_NAME,'button')
    login_button.click()


@then(u'User should see dashboard in current page URL')
def step_validate_dashboard_url(context):
    current_page_url = context.driver.current_url
    print(context.driver.current_url)
    assert "dashboard" in current_page_url, "Login Failed"
    
    
@when(u'User enters username {username}')
def step_enter_username_parameter(context, username):
    username_textbox = context.wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
    username_textbox.send_keys(username)


@when(u'User enters password {password}')
def step_enter_password_parameter(context, password):
    password_textbox = context.wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
    password_textbox.send_keys(password)
