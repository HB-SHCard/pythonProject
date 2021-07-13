import sys
import time
from enum import Enum

import pyautogui as pag
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class OptionType(Enum):
    COMB = 1
    GROUP = 2


def buy_something_from_gmarket(item_code: str, option_type: OptionType = OptionType.COMB) -> bool:
    # 로그인 주소 선언
    url = 'https://mobile.gmarket.co.kr/Login/Login?' \
          'URL=https%3A%2F%2Fm.gmarket.co.kr'
    # 웹 드라이버 로드
    driver = webdriver.Chrome('./chromedriver')
    # 30초 타임 아웃
    driver.implicitly_wait(10)
    # 로그인 주소로 이동
    driver.get(url)
    print(driver.current_url)
    try:
        # 아이디 패스워드 입력
        driver.find_element_by_id('id').send_keys('ravens')
        driver.find_element_by_id('pwd').send_keys('gmkrptxk!!38')
        # 로그인 버튼 클릭
        driver.find_element_by_id('btnLogin').click()
        # 로그인 확인
        driver.find_element_by_xpath('//button[@class="button__search"]')
        # 판매 페이지로 이동 http://mitem.gmarket.co.kr/Item?goodscode=2081880271
        driver.get('http://mitem.gmarket.co.kr/Item?goodscode=' + item_code)
        # 바로 구매 클릭
        driver.find_element_by_xpath('//a[@class="immt button"]').click()
        driver.implicitly_wait(3)
        # 옵션의 갯수를 얻는다.
        options = driver.find_elements_by_xpath(
            '//*[@id="scroll_cont_wrap"]/div/div/div[starts-with(@class, "option-item")]')
        print('options count: ' + str(len(options)))
        # 옵션의 갯수만큼 클릭
        for ii in range(len(options)):
            driver.find_element_by_xpath('//*[@id="scroll_cont_wrap"]/div/div/div[' + str(ii + 1) + ']/button').click()
            if option_type == OptionType.COMB:
                driver.find_element_by_xpath('//*[@id="combOptionList_' + str(ii) + '"]/ul/li[1]').click()
            else:
                # 그룹 아이템 리스트일 경우
                driver.find_element_by_xpath('//*[@id="groupItemList"]/ul/li[1]').click()
                # 수량 선택
                driver.find_element_by_xpath('//*[@id="scroll_cont_wrap"]/div/div/div[2]/button').click()

        # 바로 구매 클릭
        driver.find_element_by_xpath('//a[@class="immt"]').click()
        driver.implicitly_wait(10)
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
        # 주문 완료 창 로드 확인
        time.sleep(10)
        driver.find_element_by_xpath('//*[@id="content"]/section[4]/div/a[1]')
    except NoSuchElementException as e:
        print(e)
        is_success = False
    except:
        print("Unexpected error:", sys.exc_info()[0])
        is_success = False
    else:
        is_success = True
    finally:
        # 종료
        driver.close()

    return is_success


if __name__ == "__main__":
    for i in range(10):
        if buy_something_from_gmarket('2071272665', OptionType.GROUP):
            break
