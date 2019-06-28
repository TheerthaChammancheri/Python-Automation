import unittest
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


class Orange_HRM(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.get('https://www.amazon.in')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_User(self):
        self.driver.find_element_by_name('field-keywords').send_keys('Mobiles under 15000 rupees')
        action=ActionChains(self.driver)
        self.driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input').click()
        time.sleep(5)
        option=self.driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span')
        self.driver.execute_script("arguments[0].scrollIntoView();",option)
        option.click()
        time.sleep(5)

if __name__=='__main__':
    unittest.main() 