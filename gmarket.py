import time

import pyautogui as pag
from selenium import webdriver

# 로그인 주소 선언
URL = 'https://mobile.gmarket.co.kr/Login/Login?' \
      'URL=https%3A%2F%2Fm.gmarket.co.kr'
# 웹 드라이버 로드
driver = webdriver.Chrome('./chromedriver')
# 10초 타임 아웃
driver.implicitly_wait(10)
# 로그인 주소로 이동
driver.get(URL)
print(driver.current_url)
# 아이디 패스워드 입력
driver.find_element_by_id('id').send_keys('ravens')
driver.find_element_by_id('pwd').send_keys('gmkrptxk!!38')
# 로그인 버튼 클릭
driver.find_element_by_id('btnLogin').click()
# 로그인 확인
driver.find_element_by_xpath('/html/body/div/div/header/div/div[5]/div/button')
# 판매 페이지로 이동
driver.get('http://mitem.gmarket.co.kr/Item?goodscode=2098526306')
# 바로 구매 클릭
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[7]/div[1]/div/div/span[1]/a').click()
# 판매 옵션1 선택
driver.find_element_by_xpath('//*[@id="scroll_cont_wrap"]/div/div/div[1]/button').click()
driver.find_element_by_xpath('//*[@id="combOptionList_0"]/ul/li[1]/label').click()
# 판매 옵션2 선택
driver.find_element_by_xpath('//*[@id="scroll_cont_wrap"]/div/div/div[2]/button').click()
driver.find_element_by_xpath('//*[@id="combOptionList_1"]/ul/li[1]/label').click()
# 바로 구매 클릭
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[7]/div[2]/div/div/div[2]/div[2]/div[1]/div/span[1]/a').click()
# 결제 페이지에서 결제하기 버튼 클릭
driver.find_element_by_id('payment-button').click()
# 스마일페이 창 로드 확인
driver.find_element_by_id('newSmilePayFrame')
driver.switch_to.frame('newSmilePayFrame')
driver.find_element_by_xpath('//*[@id="securityKey"]/button[1]/span')
# 스마일페이 비밀번호 입력
target = {}
x, y = pag.locateCenterOnScreen('kpd/smile/8.png', confidence=0.9)
target['8'] = [x // 2, y // 2]  # mac os hidpi 기능으로 인해 화면 해상도와 스크린샷 이미지 파일의 해상도가 2배 차이나서 2로 나눈다
x, y = pag.locateCenterOnScreen('kpd/smile/6.png', confidence=0.9)
target['6'] = [x // 2, y // 2]
print(target)

pag.click(x=target['8'][0], y=target['8'][1])
pag.click(x=target['6'][0], y=target['6'][1])
pag.click(x=target['6'][0], y=target['6'][1])
pag.click(x=target['8'][0], y=target['8'][1])
pag.click(x=target['8'][0], y=target['8'][1])
pag.click(x=target['6'][0], y=target['6'][1])
