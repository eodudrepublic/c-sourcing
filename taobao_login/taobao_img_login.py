from selenium.webdriver.common.by import By  # 웹 페이지의 요소를 지정하는 방법을 정의
from selenium.webdriver.common.keys import Keys  # 키보드 키 액션을 시뮬레이션하는데 사용
import time
from copy_img.copy_naver_img import naver_img


def taobao_link_login(element_img, browser):
    # 키워드 입력 -> 주어진 이미지 URL을 이용해 이미지를 클립보드에 복사하는 naver_img 함수 호출
    naver_img(element_img)

    # 타오바오 메인 페이지로 이동
    url = 'https://taobao.com'
    browser.get(url)
    browser.implicitly_wait(10)  # 페이지 요소가 로드될 때까지 최대 10초간 대기
    time.sleep(1)

    # 검색어 입력 -> # 이미지 검색창 찾기 및 클릭
    try:
        search = browser.find_element(By.XPATH,
                                      '//*[@id="root"]/div[3]/div[1]/div[2]/div[1]/input')  # taobao 이미지 등록 search 창 -> 타오바오 이미지 등록 검색창의 XPath
        search.click()
        time.sleep(2)
    except:
        search = browser.find_element(By.XPATH,
                                      '//*[@id="root"]/div[2]/div[1]/div[2]/div[1]/input')  # taobao 이미지 등록 search 창 -> 대체 XPath 사용
        search.click()
        time.sleep(2)

    # 클립보드의 이미지를 검색창에 붙여넣기
    search.send_keys(Keys.CONTROL + "v")
    time.sleep(2)

    # 이미지 검색 버튼 클릭
    img_search_button = browser.find_element(By.CSS_SELECTOR, "div.component-preview-button")
    img_search_button.click()

    # 페이지 로딩 대기
    browser.implicitly_wait(3)

    # 새 창이 열릴 때까지 대기 후, 새 창으로 전환
    while len(browser.window_handles) == 1:
        time.sleep(0.5)
        # 여러 개의 창이 있는 경우에만 원래 창을 닫음
    if len(browser.window_handles) > 1:
        browser.close()
        time.sleep(0.5)

    # 새 창으로 전환
    browser.switch_to.window(browser.window_handles[-1])
    time.sleep(90)  # 긴 대기시간 -> 이 시간동안 로그인 완료해야함
