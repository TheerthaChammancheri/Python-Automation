from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

driver.get('file:///E:/Subash/Python/SeleniumAutomation/Resources/Webtable.html')

# number of rows in a table
rows = len(driver.find_elements_by_xpath('/html/body/table/tbody/tr'))

# number of columns
cols = len(driver.find_elements_by_xpath('/html/body/table/tbody/tr[1]/th'))

for r in range(2, rows+1):
    for c in range(1, cols+1):
        value = driver.find_element_by_xpath('/html/body/table/tbody/tr[{}]/td[{}]'.format(r, c)).text
        print value, end='  '
    print ()

driver.quit()