from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
driver.get('http://newtours.demoaut.com')
driver.maximize_window()
links=driver.find_elements_by_tag_name('a')
cnt=len(links)
print cnt
for x in links:
    print x.text
time.sleep(5)
driver.close()
driver.quit()