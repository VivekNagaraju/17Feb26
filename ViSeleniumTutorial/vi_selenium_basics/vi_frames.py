'''
Created on 26-Apr-2026

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
driver.get("https://demo.automationtesting.in/Frames.html")

'''3. Switch to the iFrame'''
driver.switch_to.frame('singleframe')

'''4. Enter text in text field inside frame'''
input_single_frame = driver.find_element(By.TAG_NAME, 'input')
input_single_frame.send_keys("Vivek")
