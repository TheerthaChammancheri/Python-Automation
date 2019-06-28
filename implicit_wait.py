from selenium import webdriver

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe')

driver.get('http://newtours.demoaut.com')

# implicit wait
driver.implicitly_wait(10)

driver.find_element_by_name('userName').send_keys('mercury')
driver.find_element_by_name('password').send_keys('mercury')

driver.find_element_by_name('login').click()