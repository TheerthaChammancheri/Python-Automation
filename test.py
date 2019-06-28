from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import unittest

class Testcase1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_TC1(self):
        self.driver.find_element_by_name('txtUsername').send_keys('Admin')
        self.driver.find_element_by_name('txtPassword').send_keys('admin123')
        self.driver.find_element_by_name('Submit').click()
        self.obj1 = self.driver.find_element_by_xpath('//*[@id="menu__Performance"]/b')
        self.obj2 = self.driver.find_element_by_xpath('//*[@id="menu_performance_Configure"]')
        self.obj3 = self.driver.find_element_by_xpath('//*[@id="menu_performance_addPerformanceTracker"]')

        actions = ActionChains(self.driver)
        actions.move_to_element(self.obj1).move_to_element(self.obj2).move_to_element(self.obj3).click().perform()
    def validate(self):
        self.assertEqual(self.driver.title == 'OrangeHRM', 'Failed')

if __name__=='__main__':
    unittest.main()



