from selenium import webdriver  # 웹 브라우저를 자동화하기 위한 모듈
from selenium.webdriver.support.ui import WebDriverWait  # 웹 요소가 로드될 때까지 기다리는 기능 제공
from selenium.webdriver.chrome.service import Service  # 크롬 드라이버 서비스를 관리하는데 사용

# ------------------------------------1------------------------------------
# taobao_link_login 함수 : 프로그램이 시작될때, 임시 이미지(현재 피카츄)로 검색해 로그인 창을 띄우고, 긴 대기시간동안 로그인을 완료해야 하는 함수
from taobao_login.taobao_img_login import taobao_link_login

# ------------------------------------2------------------------------------
from sourcing.check_banned_words import load_banned_words, check_words_in_sentence

all_banned_words = load_banned_words('./ban_word.csv')  # 모든 금칙 상표권

# tao_sourcing 함수 : 네이버에서 조사한 내용을 바탕으로 타오바오에서 해당 키워드의 이미지로 소싱 작업을 수행하는 함수
from sourcing.taobao_sourcing_to_excel import taobao_sourcing


# ------------------------------------3------------------------------------
def start_sourcing(banned_words, _browser):
    while True:
        # "url.txt" 파일을 열어 키워드를 읽음
        with open("./url.txt", "r", encoding='utf-8') as f:
            lines = f.readlines()  # 파일의 모든 라인을 읽어 리스트로 저장

        try:
            if not lines:
                print("소싱이 완료되었습니다.")
                break

            # 첫 줄에 앞뒤 공백을 제거한 키워드를 읽음
            competitor = lines.pop(0).strip()

            if competitor == '':  # 빈 키워드라면 건너뛰기
                print("경쟁사 url이 없습니다")
            else:
                print(f"Competitor : {competitor}")
                taobao_sourcing(competitor, banned_words, _browser)  # 각 url에 대해 taobao_sourcing 함수 호출

            # 소싱한 경쟁사 링크를 제외한 나머지 url들을 다시 파일에 씀
            with open("./url.txt", "w", encoding='utf-8') as f:
                f.writelines(lines)

        except:
            print("not txt")  # 파일 읽기 중 에러 발생 시 출력
            pass



# -------------------실행 1-------------------
# browser 객체를 세팅하는 set_browser 함수를 만들어야 할까?
# Selenium 라이브러리를 사용하여 Chrome 웹드라이버를 설정하고 초기화 -> 크롬 브라우저를 자동화하기 위한 설정 => 웹 페이지의 자동화된 테스트 및 데이터 스크래핑에 주로 사용
# Selenium을 사용하기 위한 Chrome 웹드라이버 서비스 설정
service = Service(executable_path=r'./chromedriver-win64/chromedriver.exe')
# 위 코드는 현재 디렉토리 내의 chromedriver 경로를 지정합니다.

# Chrome 브라우저 옵션 설정
options = webdriver.ChromeOptions()

# 사용자 에이전트를 설정하여, Selenium 스크립트가 웹 브라우저에서 자동으로 실행되는 것처럼 보이게 합니다.
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36")

# 웹드라이버가 자동화된 것처럼 보이지 않도록 하는 옵션 추가
options.add_argument("--disable-blink-features=AutomationControlled")

# Selenium이 자동화된 것으로 탐지되는 것을 방지하기 위한 추가적인 옵션 설정
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# 위에서 설정한 서비스와 옵션을 사용하여 Chrome 웹드라이버 인스턴스 생성
browser = webdriver.Chrome(service=service, options=options)

# 웹 요소가 로드될 때까지 최대 5초간 기다리는 WebDriverWait 객체 생성 -> 웹 페이지가 완전히 로드될 때까지 기다리거나 특정 요소가 로드될 때까지 기다릴 필요가 있을 때 사용
wait = WebDriverWait(browser, 5)

# -------------------실행 2-------------------
taobao_link_login(
    "https://shop-phinf.pstatic.net/20230807_298/1691374422549Bw9Yv_JPEG/6386509650415096_102927579.jpg?type=m510",
    browser)
start_sourcing(all_banned_words, browser)
