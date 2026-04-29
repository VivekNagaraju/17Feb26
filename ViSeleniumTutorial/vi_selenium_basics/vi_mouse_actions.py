'''
Created on 28-Apr-2026

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

'''3. Create actions object from ActionChains class'''
actions = ActionChains(driver)

'''4. Double click'''
copy_text_btn = driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')
driver.execute_script("var evt = new MouseEvent('dblclick', {bubbles: true, cancelable: true}); arguments[0].dispatchEvent(evt);", copy_text_btn)


'''5. Mouse Hovering'''
# Locate the element
# point_me_btn = driver.find_element(By.CLASS_NAME, 'dropbtn')
# actions.move_to_element(point_me_btn).perform()
