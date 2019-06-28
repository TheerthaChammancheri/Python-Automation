from selenium import webdriver

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

driver.get('https://testautomationpractice.blogspot.com/')

# to click on ok
driver.switch_to_alert().accept()
# to click on cancel
driver.switch_to_alert().dismiss()

driver.close()
driver.quit()