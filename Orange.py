import unittest
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

class Orange(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.get('https://opensource-demo.orangehrmlive.com/')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login(self):
        self.driver.find_element_by_name('txtUsername').send_keys('Admin')
        self.driver.find_element_by_name('txtPassword').send_keys('admin123')
        self.driver.find_element_by_name('Submit').click()
        time.sleep(2)
        #Add the new user
        admin=self.driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')
        usermgmt = self.driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
        users = self.driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')
        action = ActionChains(self.driver)
        action.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()
        self.driver.find_element_by_name('btnAdd').click()
        self.driver.find_element_by_xpath('//*[@id="systemUser_employeeName_empName"]').send_keys('Fiona Grace')
        self.driver.find_element_by_name('systemUser[userName]').send_keys('Grace_fiona')
        self.driver.find_element_by_name('systemUser[password]').send_keys('1234ABCD!@#$')
        self.driver.find_element_by_name('systemUser[confirmPassword]').send_keys('1234ABCD!@#$')
        self.driver.find_element_by_name('btnSave').click()
        time.sleep(2)
        #Leave report
        Leave = self.driver.find_element_by_xpath('//*[@id="menu_leave_viewLeaveModule"]/b')
        reports = self.driver.find_element_by_xpath('//*[@id="menu_leave_Reports"]')
        usage_report= self.driver.find_element_by_xpath('//*[@id="menu_leave_viewLeaveBalanceReport"]')
        action = ActionChains(self.driver)
        action.move_to_element(Leave).move_to_element(reports).move_to_element(usage_report).click().perform()
        drpdwn=Select(self.driver.find_element_by_name('leave_balance[report_type]'))
        drpdwn.select_by_visible_text('Employee')
        time.sleep(2)
        self.driver.find_element_by_name('leave_balance[employee][empName]').send_keys('Fiona Grace')
        self.driver.find_element_by_xpath('/html/body/div[4]/ul/li').click()
        drpdwwn=Select(self.driver.find_element_by_xpath('//*[@id="period"]'))
        drpdwwn.select_by_visible_text('01-2019-01 - 31-2019-12')
        time.sleep(2)
        self.driver.find_element_by_name('view').click()
        time.sleep(5)


if __name__=='__main__':
        unittest.main()