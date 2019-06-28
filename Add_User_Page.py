class Add_User():

    employee_name_xpath='//*[@id="systemUser_employeeName_empName"]'
    username_name='systemUser[userName]'
    password_name='systemUser[password]'
    confirm_password_name='systemUser[confirmPassword]'
    save_button_name='btnSave'

    def __init__(self,driver):
        self.driver=driver

    def add_users(self,emp_name,user_name,pswd):
        self.driver.find_element_by_xpath(self.employee_name_xpath).send_keys(emp_name)
        self.driver.find_element_by_name(self.username_name).send_keys(user_name)
        self.driver.find_element_by_name(self.password_name).send_keys(pswd)