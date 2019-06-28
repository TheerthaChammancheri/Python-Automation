from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
driver.maximize_window()

src_ele = driver.find_element_by_xpath('//*[@id="box6"]')
dest_ele = driver.find_element_by_xpath('//*[@id="box106"]')

actions = ActionChains(driver)
actions.drag_and_drop(src_ele, dest_ele).perform()
time.sleep(5)

driver.quit()