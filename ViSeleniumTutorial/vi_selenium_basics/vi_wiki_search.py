'''
Created on 15-Apr-2026

@author: admin
'''
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

'''3. Wiki search'''
'''3a. Enter text'''
wiki_search_txtbx = driver.find_element(By.ID, 'Wikipedia1_wikipedia-search-input')
wiki_search_txtbx.send_keys("Selenium")

'''3b. Click on search icon'''
wiki_search_icon = driver.find_element(By.CLASS_NAME, 'wikipedia-search-button')
wiki_search_icon.click()