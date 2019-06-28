class Login_PageObjects():
    Username_name='txtUsername'
    Password_name='txtPassword'
    Login_button_name='Submit'
    Forgot_password_xpath='//*[@id="forgotPasswordLink"]/a'

    def __init__(self,driver):
        self.driver=driver

    def set_Username(self,Username):
        self.driver.find_element_by_name(self.Username_name).send_keys(Username)

    def set_pswd(self,password):
        self.driver.find_element_by_name(self.Password_name).send_keys(password)

    def login_Button(self):
        self.driver.find_element_by_name(self.Login_button_name).click()

    def forgot_pwd(self):
        self.driver.find_element_by_xpath(self.Forgot_password_xpath).click()


