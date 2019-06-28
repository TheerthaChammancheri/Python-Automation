from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()

driver.find_element_by_id('txtUsername').send_keys('Admin')
driver.find_element_by_id('txtPassword').send_keys('admin123')
driver.find_element_by_id('btnLogin').click()

admin = driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')
usrmgt = driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
users = driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')

actions = ActionChains(driver)

actions.move_to_element(admin).move_to_element(usrmgt).move_to_element(users).click().perform()
time.sleep(10)

driver.quit()