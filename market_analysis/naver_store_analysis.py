from selenium.webdriver.common.by import By  # 웹 페이지의 요소를 지정하는 방법을 정의
import time  # 시간과 관련된 기능 제공


# 제공받은 경쟁사 url로 접속하여 베스트셀러 제품을 가져오는 함수
def competitor_sourcing(competitor, _browser):
    sort_p = []  # 추출된 베스트셀러 제품 링크를 저장할 리스트

    try:
        time.sleep(0.5)  # 짧은 지연시간 추가
        # 경쟁사 스마트스토어의 인기 상품 페이지 URL 생성
        url = competitor
        print(f"Competitor URL: {url}")  # 디버깅을 위해 방문하는 URL 출력
        _browser.get(url=url)  # 해당 URL로 이동
        _browser.implicitly_wait(10)  # 페이지 로딩 대기

        token = False  # 'NEW' 제품이 있는지 확인하기 위한 토큰
        try:
            # 페이지 내 제품 요소들을 찾음
            product_selects = _browser.find_elements(By.CSS_SELECTOR, 'div._2kRKWS_t1E')
            # 'NEW' 또는 '신상' 키워드가 포함된 제품이 있는지 확인
            for product_select in product_selects:
                texter = product_select.text
                if any(keyword in texter for keyword in ['NEW', 'new', 'New', '신상']):
                    token = True
                    break

            # 'NEW' 제품이 있다면, 'BEST' 제품 링크를 수집
            if token:
                for product_select in product_selects:
                    texter = product_select.text
                    if any(keyword in texter for keyword in ['BEST', 'Best', 'best', '베스트']):
                        # 해당 제품의 링크를 추출하여 저장
                        sort_p.append(product_select.find_element(By.TAG_NAME, 'a').get_attribute('href'))
                        print(product_select.find_element(By.TAG_NAME, 'a').get_attribute('href'))

            token = False  # 토큰 리셋
        except:
            print(f"An error occurred:")  # 오류 발생 시 메시지 출력
            pass
    except:
        pass

    return sort_p  # 추출된 베스트셀러 제품 링크 반환
