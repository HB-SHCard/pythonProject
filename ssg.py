import time

import pyautogui as pag
from selenium import webdriver

URL = 'https://member.ssg.com/m/member/login.ssg?' \
      'retURL=http%3A%2F%2Fm.ssg.com%2Fitem%2FitemView.ssg%3FitemId%3D1000033892210'

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(10)
driver.get(URL)
print(driver.current_url)
driver.find_element_by_id('inp_id').send_keys('bitterdeath')
driver.find_element_by_id('inp_pw').send_keys('ssgrptxk!!38')
driver.find_element_by_xpath('//button[@type="submit"]').click()
driver.find_element_by_id('actionPayment').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="_cpay_ssgpay_slider"]/div[1]/button[2]').click()
driver.find_element_by_xpath('//*[@id="_codr_opt_bar"]/div/div[3]/div/span/label').click()
driver.find_element_by_xpath('//*[@id="_codr_opt_bar"]/div/div[3]/button').click()
time.sleep(3)

target = {}
x, y = pag.locateCenterOnScreen('kpd/ssg/8.png', confidence=0.9)
target['8'] = [x // 2, y // 2]  # mac os hidpi 기능으로 인해 화면 해상도와 스크린샷 이미지 파일의 해상도가 2배 차이나서 2로 나눈다
x, y = pag.locateCenterOnScreen('kpd/ssg/6.png', confidence=0.9)
target['6'] = [x // 2, y // 2]
print(target)

pag.click(x=target['8'][0], y=target['8'][1])
pag.click(x=target['6'][0], y=target['6'][1])
pag.click(x=target['6'][0], y=target['6'][1])
pag.click(x=target['8'][0], y=target['8'][1])
pag.click(x=target['8'][0], y=target['8'][1])
pag.click(x=target['6'][0], y=target['6'][1])
