from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrmOptions = Options()
chrmOptions.add_experimental_option('prefs', {'download.default_directory' :
                                                  'E:/Subash/Python/SeleniumAutomation/Resources/'})

driver = webdriver.Chrome(executable_path='../driver/chromedriver.exe', chrome_options=chrmOptions)
driver.maximize_window()

driver.get('http://demo.automationtesting.in/FileDownload.html')
driver.maximize_window()

# Enter the text in the text area
driver.find_element_by_xpath('//*[@id="textbox"]').send_keys('Testing the Download feature for text file')
# Click on the generate file button for Text file
time.sleep(2)
driver.find_element_by_id('createTxt').click()
driver.find_element_by_id('link-to-download').click()
time.sleep(5)

# Enter the text in the text area
driver.find_element_by_xpath('//*[@id="pdfbox"]').send_keys('Testing the Download feature for PDF file')
time.sleep(2)
# Click on the generate file button for pdf file
driver.find_element_by_id('createPdf').click()
driver.find_element_by_id('pdf-link-to-download').click()
time.sleep(5)

driver.close()
driver.quit()