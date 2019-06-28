# automation for "OrangeHRM"

from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
#open the webpage
driver=webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
#login
driver.find_element_by_name('txtUsername').send_keys('Admin')
driver.find_element_by_name('txtPassword').send_keys('admin123')
driver.find_element_by_name('Submit').click()
#go to users data
admin=driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')
usermgmt=driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
users=driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')
action=ActionChains(driver)
action.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()
#select a user
driver.find_element_by_name('searchSystemUser[userName]').send_keys('fiona.gracee')
usrtype=Select(driver.find_element_by_name('searchSystemUser[userType]'))
usrtype.select_by_visible_text('ESS')
driver.find_element_by_name('searchSystemUser[employeeName][empName]').send_keys('Fiona Grace')
status=Select(driver.find_element_by_name('searchSystemUser[status]'))
status.select_by_visible_text('Enabled')
driver.find_element_by_name('_search').click()
#Check user details
#driver.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr[2]/td[2]/a').click()
driver.find_element_by_xpath('//*[@id="resultTable"]/tbody/tr/td[2]/a').click()
driver.find_element_by_xpath('//*[@id="btnSave"]').click()
driver.find_element_by_name('systemUser[userName]').clear()
driver.find_element_by_name('systemUser[userName]').send_keys('fiona.grace')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="btnSave"]').click()

time.sleep(5)
driver.close()
driver.quit()