from selenium.webdriver import ActionChains
class Logout():

    welcome_button_xpath='//*[@id="welcome"]'
    logout_button_xpath='//*[@id="welcome-menu"]/ul/li[2]/a'

    def __init__(self,driver):
        self.driver=driver

    def logout(self):
        welcome_click=self.driver.find_element_by_xpath(self.welcome_button_xpath)
        logout_click=self.driver.find_element_by_xpath(self.logout_button_xpath)
        action=ActionChains(self.driver)
        action.move_to_element(welcome_click).move_to_element(logout_click).click().perform()

