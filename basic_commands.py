from selenium import webdriver
import time

# create an instant of driver
driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

# open the url
driver.get('http://demo.automationtesting.in/Windows.html')

# maximize the window
driver.maximize_window()

# return the tile of the webpage
print (driver.title)

# return the url of the webpage
print (driver.current_url)

# Click on button
driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()
time.sleep(5)

driver.close() # will close only current browser
driver.quit() # will close all the browser windows