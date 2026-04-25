'''
Created on 25-Apr-2026

@author: Vivek
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''1. Launch Chrome browser'''

# Defining the browser Settings
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

# Creating webdriver object
driver = webdriver.Chrome(options)
driver.implicitly_wait(20)

'''2. Navigating to a web page'''
driver.get("https://testautomationpractice.blogspot.com/")

'''3. Click on Simple Alert button'''
simple_alert_btn = driver.find_element(By.ID, "alertBtn")
simple_alert_btn.click()

'''4. Switch to the alert popup'''
alert_popup = driver.switch_to.alert

time.sleep(2)
'''5. Click on OK in the alert present'''
alert_popup.accept()
