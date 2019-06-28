from selenium import webdriver
import unittest
import time
from Pages.Login_Page import Login_PageObjects
from selenium.webdriver import ActionChains
from Pages.Admin_Page import Admin
from Pages.Logout_Page import Logout

class Login_Test(unittest.TestCase):

    baseUrl='https://opensource-demo.orangehrmlive.com'
    Username='Admin'
    Password='admin123'
    driver = webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseUrl)
        cls.driver.maximize_window()
        LP = Login_PageObjects(cls.driver)
        LP.set_Username(cls.Username)
        LP.set_pswd(cls.Password)
        LP.login_Button()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        LO=Logout(cls.driver)
        LO.logout()
        cls.driver.quit()

    # unittest.skipIf(driver.current_url=='https://opensource-demo.orangehrmlive.com/index.php/dashboard')
    # def test_zforgot_pwd(self):
    #     LP = Login_PageObjects(self.driver)
    #     LP.Forgot_pwd()

    def test_admin_search_user(self):
        admin =self.driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')
        user_mgmt=self.driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
        users = self.driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')
        action=ActionChains(self.driver)
        action.move_to_element(admin).move_to_element(user_mgmt).move_to_element(users).click().perform()
        time.sleep(2)
        username='fiona.grace'
        userrole='ESS'
        employeename='Fiona Grace'
        status='Enabled'
        AP=Admin(self.driver)
        AP.set_username(username)
        AP.set_userrole(userrole)
        AP.set_employeename(employeename)
        AP.status(status)
        AP.search()
        time.sleep(2)

    def test_admin_add_user(self):
        admin = self.driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')
        user_mgmt = self.driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
        users = self.driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')
        action = ActionChains(self.driver)
        action.move_to_element(admin).move_to_element(user_mgmt).move_to_element(users).click().perform()
        time.sleep(2)
        AP = Admin(self.driver)
        AP.add()


if __name__=='__main__':
    unittest.main()

