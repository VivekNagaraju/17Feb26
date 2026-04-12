'''
Created on 12-Apr-2026

@author: Vivek
'''
from selenium import webdriver

'''1. Launch Chrome browser'''

# Defining the browser Settings
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

# Creating webdriver object
driver = webdriver.Chrome(options)

'''2. Navigating to a web page'''
driver.get("https://www.selenium.dev/")

'''3. Print the current page title'''
current_page_title = driver.title
print("current_page_title:", current_page_title)

