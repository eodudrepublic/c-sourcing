from selenium.webdriver.support import expected_conditions as EC  # 특정 웹 요소의 상태를 확인하는 조건들 제공
from selenium.webdriver.common.by import By  # 웹 페이지의 요소를 지정하는 방법을 정의
from selenium.webdriver.support.ui import WebDriverWait  # 웹 요소가 로드될 때까지 기다리는 기능 제공
import time  # 시간과 관련된 기능 제공
from random import random  # 무작위 수를 생성하는데 사용
import random  # 무작위와 관련된 여러 기능을 제공하는 모듈


# 미리 정의한 id, 비밀번호로 타오바오 사이트에 자동으로 로그인하는 함수
# -> 이게 두현님이 원하는 기능이긴 한데, 레온님 말대로는 이대로 하면 캡챠띄운다고 함 => 일단 활용해봐야할듯
def taobao_login(browser):
    url = 'https://login.taobao.com/member/login.jhtml'  # 타오바오 로그인 페이지 URL
    browser.get(url=url)  # Selenium 웹 드라이버를 사용하여 로그인 페이지로 이동
    browser.implicitly_wait(10)  # 웹 페이지 요소가 로드될 때까지 최대 10초간 대기

    # 웹 요소가 로드될 때까지 최대 5초간 기다리는 WebDriverWait 객체 생성 -> 웹 페이지가 완전히 로드될 때까지 기다리거나 특정 요소가 로드될 때까지 기다릴 필요가 있을 때 사용
    wait = WebDriverWait(browser, 5)

    # 사용자 이름 입력 필드 찾기
    id_input = wait.until(EC.presence_of_element_located((By.ID, "fm-login-id")))
    id_input.send_keys('tb791015072')  # 사용자 이름 입력
    time.sleep(1)  # 입력 사이에 짧은 지연 시간 추가

    # 비밀번호 입력 필드 찾기
    pw_input = wait.until(EC.presence_of_element_located((By.ID, "fm-login-password")))
    pw_input.send_keys('kt016923')  # 비밀번호 입력
    time.sleep(1)  # 입력 사이에 짧은 지연 시간 추가

    # 로그인 버튼 클릭
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "fm-button"))).click()

    # 로그인 처리가 완료될 때까지 잠시 대기
    time.sleep(random.randint(5, 10))
    # 이 함수는 타오바오 로그인 페이지에 접근하여 자동으로 로그인 절차를 수행합니다.
