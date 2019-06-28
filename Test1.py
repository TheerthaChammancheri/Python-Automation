from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
driver.find_element_by_name('txtUsername').send_keys('Admin')
driver.find_element_by_name('txtPassword').send_keys('admin123')
driver.find_element_by_name('Submit').click()


time.sleep((10))
driver.close()
driver.quit()