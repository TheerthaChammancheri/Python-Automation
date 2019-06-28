from selenium.webdriver.support.ui import Select


class Admin():

    username_inputbox_name='searchSystemUser[userName]'
    userrole_drpdwn_name='searchSystemUser[userType]'
    employee_name_inputbox_name='searchSystemUser[employeeName][empName]'
    status_drpdwn_name='searchSystemUser[status]'
    search_button_name='_search'
    reset_button_name='_reset'
    add_button_name='btnAdd'
    delete_button_name='btnDelete'

    def __init__(self,driver):
        self.driver=driver

    def set_username(self,username):
        self.driver.find_element_by_name(self.username_inputbox_name).send_keys(username)

    def set_userrole(self,value):
        drp=Select(self.driver.find_element_by_name(self.userrole_drpdwn_name))
        drp.select_by_visible_text(value)

    def set_employeename(self,name):
        self.driver.find_element_by_name(self.employee_name_inputbox_name).send_keys(name)

    def status(self,value):
        drp = Select(self.driver.find_element_by_name(self. status_drpdwn_name))
        drp.select_by_visible_text(value)

    def search(self):
        self.driver.find_element_by_name(self.search_button_name).click()

    def reset(self):
        self.driver.find_element_by_name(self.reset_button_name).click()

    def add(self):
        self.driver.find_element_by_name(self.add_button_name).click()

    def delete(self):
        self.driver.find_element_by_name(self.delete_button_name).click()
