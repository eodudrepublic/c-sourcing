from bs4 import BeautifulSoup
import json


def soup_category(browser):
    # 페이지의 소스코드를 가져와 BeautifulSoup으로 파싱
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")

    # <head> 태그 내의 <script> 태그에서 원하는 정보 추출
    script_tag = soup.find("script", {"type": "application/ld+json"})
    if script_tag:
        script_content = script_tag.string.strip()

        # JSON 형식의 데이터로 변환
        data = json.loads(script_content)

        # 필요한 정보 추출
        name = data["name"]
        image = data["image"]
        category = data["category"]
        price = data["offers"]["price"]

        # 추출한 정보 출력
        print("상품명:", name)
        print("이미지 URL:", image)
        print("카테고리:", category)
        print("가격:", price)

        return category

    else:
        # 오류 상황 추가
        return None
