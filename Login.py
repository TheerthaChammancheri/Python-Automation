import unittest
from selenium import webdriver
import time

class Login(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.driver.maximize_window()

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.find_element_by_name('txtUsername').send_keys('Admin')
        self.driver.find_element_by_name('txtPassword').send_keys('admin123')
        self.driver.find_element_by_name('Submit').click()
        time.sleep(5)

if __name__=='__main__':
        unittest.main()
