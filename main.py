from selenium import webdriver


URL = 'https://www.shinhancard.com'

driver = webdriver.Chrome('./chromedriver')
driver.get(url=URL)
print(driver.current_url)
driver.close()
