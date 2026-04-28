'''
Created on 28-Apr-2026

@author: Vivek
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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

'''3. Create actions object from ActionChains class'''
actions = ActionChains(driver)

'''4. Double click'''
copy_text_btn = driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')
actions.double_click(copy_text_btn).perform()

'''5. Mouse Hovering'''
# Locate the element
point_me_btn = driver.find_element(By.CLASS_NAME, 'dropbtn')
actions.move_to_element(point_me_btn).perform()
