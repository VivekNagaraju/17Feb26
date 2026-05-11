'''
Created on 11-May-2026

@author: Vivek
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

'''1. Launch Chrome browser'''

# Defining the browser Settings
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

# Creating webdriver object
driver = webdriver.Chrome(options)
driver.implicitly_wait(20)

'''1a. Explicit wait'''
# 1a.1. Create an object from WebDriverWait class
wait = WebDriverWait(driver, timeout=5)

'''2. Navigating to a web page'''
driver.get("https://testautomationpractice.blogspot.com/")

'''3. Enter date in date picker 2'''
# date_picker_2 = driver.find_element(By.ID, 'txtDate')
# date_picker_2.send_keys("11/05/2026")
# driver.execute_script('document.getElementById(arguments[0]).value=arguments[1];', "txtDate", "11/05/2026")
driver.execute_script('document.getElementById("txtDate").value="11/05/2026";')




# document.getElementById("txtDate").removeAttribute("readonly")