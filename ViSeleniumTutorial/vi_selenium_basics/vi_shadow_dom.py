'''
Created on 08-May-2026

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

'''3. Locate Shadow Host element'''
shadow_host_ele = driver.find_element(By.ID, 'shadow_host')

'''4. Get the Shadow root attached to shadow host'''
shadow_root_auto = shadow_host_ele.shadow_root

'''5. Using shadow root locate the element inside shadow DOM'''
sr_input_txtbx = shadow_root_auto.find_element(By.CSS_SELECTOR, 'input[type=text]:nth-child(5)')
sr_input_txtbx.send_keys('Vivek')

'''6. Click on check box in shadow dom'''
sr_checkbx = shadow_root_auto.find_element(By.CSS_SELECTOR, 'input[type=checkbox]:nth-child(7)')
sr_checkbx.click()

'''
ins > span > svg > path
/html/body/ins[2]/div[1]//ins/span/svg/path
/html/body//*[name()='ins'][2]/div[1]//*[name()='ins']/span//*[name()='svg']//*[local-name='path']
'''