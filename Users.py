import unittest
from LOGIN.Login import Login
from selenium import webdriver
import time

Login.Login()

class users(unittest.TestCase):

    def test_users(self):
        self.driver.find_element_by_name('txtUsername').send_keys('Admin')
        self.driver.find_element_by_name('txtPassword').send_keys('admin123')
        self.driver.find_element_by_name('Submit').click()
        time.sleep(5)

if __name__=='__main__':
        unittest()