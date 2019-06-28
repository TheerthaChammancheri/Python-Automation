from selenium import webdriver

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

driver.get('http://newtours.demoaut.com')
print (driver.title)

driver.get('http://demo.automationtesting.in/Windows.html')
print (driver.title)

driver.back()
print (driver.title)

driver.forward()
print (driver.title)

driver.close()
driver.quit()