'''
Created on 04-Jun-2026

@author: admin
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginPageST(unittest.TestCase):


    def setUp(self):
        # 1. Launch Chrome browser
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("start-maximized")
        
        self.driver = webdriver.Chrome(options)
        self.driver.implicitly_wait(10)
        
        # 2. Navigate to OrangeHRM Login page
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


    def tearDown(self):
        pass


    def test_navigate_to_login_page(self):        
        # 3. Validate whether "login" is present in Current page URL
        current_page_url = self.driver.current_url
        self.assertIn("login", current_page_url, "Navigation failed")
    
    def test_login_to_orangehrm(self):        
        # 3. Enter Username
        user_wrt = self.driver.find_element(By.NAME, 'username')
        user_wrt.send_keys('admin')
        
        # 4. Enter Password
        pass_word = self.driver.find_element(By.NAME, 'password')
        pass_word.send_keys('admin123')
        
        # 5. Click on Login Button
        login_clk = self.driver.find_element(By.TAG_NAME,'button')
        login_clk.click()
        
        # 6. Validate whether "dashboard" is presnt in Current page URL
        current_page_url = self.driver.current_url
        self.assertIn("dashboard", current_page_url, "Login Failed")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()