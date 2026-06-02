'''
Created on 31-May-2026

@author: Vivek
'''
from selenium import webdriver
from selenium.webdriver.common.by import By


# 1. Launch Chrome browser
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

driver = webdriver.Chrome(options)
driver.implicitly_wait(10)

# 2. Navigate to OrangeHRM Login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# 3. Enter Username
user_wrt = driver.find_element(By.NAME, 'username')
user_wrt.send_keys('admin1')

# 4. Enter Password
pass_word = driver.find_element(By.NAME, 'password')
pass_word.send_keys('admin123')

# 5. Click on Login Button
login_clk = driver.find_element(By.TAG_NAME,'button')
login_clk.click()

# 6. Validate whether "dashboard" is presnt in Current page URL
current_page_url = driver.current_url
print(driver.current_url)
if "dashboard" in current_page_url:
    print("login passed")
else:
    print("login failed")