from selenium import webdriver
from selenium.webdriver.common.by import By

'''1. Launch Chrome browser'''

# Defining the browser Settings
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

# Creating webdriver object
driver = webdriver.Chrome(options)

'''2. Navigating to a web page'''
driver.get("https://testautomationpractice.blogspot.com/")

'''3. Enter name'''
# 3a. Locate the name text box uniquely 
enter_name_txtbx = driver.find_element(By.ID, 'name')

# 3b. Do action on the located web element
enter_name_txtbx.send_keys("Vivek")

