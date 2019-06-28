from selenium import webdriver
import time

fp = webdriver.FirefoxProfile()
fp.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/plain, application/pdf')
fp.set_preference('browser.download.manager.showWhenStarting', False)
fp.set_preference('browser.download.dir', 'E:/Subash/Python/SeleniumAutomation/Resources/')
#0 means to desktop, 1 means default and 2 means to the specified location
fp.set_preference('browser.download.folderList', 2)
# disable the pdf javascript, so that pdf file would be downloaded
fp.set_preference('pdfjs.disabled', True)

driver = webdriver.Firefox(executable_path='../driver/geckodriver.exe',
                           firefox_profile=fp)
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