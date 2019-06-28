from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

driver.get('file:///E:/Subash/Python/SeleniumAutomation/Resources/Webtable.html')
driver.maximize_window()

element = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[3]')

actions = ActionChains(driver)
actions.move_to_element(element).double_click().perform()

time.sleep(5)
driver.quit()