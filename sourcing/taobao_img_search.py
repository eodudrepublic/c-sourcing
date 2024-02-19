from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from copy_img.copy_naver_img import naver_img


def taobao_searching(element_img, browser):
    # 주어진 이미지 URL을 사용하여 클립보드에 이미지를 복사하는 naver_img 함수 호출
    naver_img(element_img)

    # 타오바오 메인 페이지로 이동
    url = 'https://taobao.com'
    browser.get(url)
    browser.implicitly_wait(10)  # 페이지 요소가 로드될 때까지 최대 10초간 대기
    time.sleep(1)

    # 타오바오의 이미지 검색창을 찾아 클릭
    try:
        search = browser.find_element(By.XPATH,
                                      '//*[@id="root"]/div[3]/div[1]/div[2]/div[1]/input')  # 타오바오 이미지 등록 검색창의 XPath
        search.click()
        time.sleep(2)
    except:
        search = browser.find_element(By.XPATH,
                                      '//*[@id="root"]/div[2]/div[1]/div[2]/div[1]/input')  # 대체 XPath 사용
        search.click()
        time.sleep(2)

    # 클립보드에 저장된 이미지를 검색창에 붙여넣기
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
        # 원래 창을 닫기
        browser.close()
        time.sleep(0.5)
    # 새 창으로 전환
    browser.switch_to.window(browser.window_handles[-1])
    time.sleep(1)  # 짧은 대기 시간

    # 타오바오에서 이미지 검색 결과 추출
    try:
        # 첫 번째 검색 결과의 제품 링크와 가격 정보를 찾아 추출
        # 제품 링크
        taobao = browser.find_element(By.XPATH, f'//*[@id="root"]/div/div[2]/div[2]/div[1]/div/a').get_attribute('href')
        print(taobao)
        # 제품 가격
        taobao_price = browser.find_element(By.XPATH,
                                            f'//*[@id="root"]/div/div[2]/div[2]/div[1]/div/a/div[3]/span[2]').text
        print(taobao_price)
        return taobao, taobao_price  # 링크와 가격 정보 반환

    except:
        # 검색 결과를 찾지 못한 경우
        print("검색결과가 없습니다")
        return "검색결과가 없습니다"
