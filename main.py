from selenium import webdriver


URL = 'https://www.shinhancard.com/mob/MOBFM001N/MOBFM001C01.shc'

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
driver.get(URL)
print(driver.current_url)
driver.find_element_by_xpath('//label[@for="install02"]').click()
driver.find_element_by_id('t01.memid').send_keys('ravens0')
print(driver.current_url)
driver.find_element_by_id('nextBtn').click()
driver.find_element_by_xpath('//label[@for="pwd"]').click()
driver.find_element_by_xpath('//img[@aria-label="특수문자"]').click()
driver.find_element_by_xpath('//img[@aria-label="우물표시"]').click()
driver.find_element_by_xpath('//img[@aria-label="소문자"]').click()
driver.find_element_by_xpath('//img[@aria-label="소문자 s"]').click()
driver.find_element_by_xpath('//img[@aria-label="소문자 h"]').click()
driver.find_element_by_xpath('//img[@aria-label="소문자 c"]').click()
driver.find_element_by_xpath('//img[@aria-label="소문자 a"]').click()
driver.find_element_by_xpath('//img[@aria-label="소문자 r"]').click()
driver.find_element_by_xpath('//img[@aria-label="소문자 d"]').click()
driver.find_element_by_xpath('//img[@aria-label="0"]').click()
driver.find_element_by_xpath('//img[@aria-label="1"]').click()
driver.find_element_by_xpath('//img[@aria-label="확인"]').click()
driver.find_element_by_id('loginBtn').click()
