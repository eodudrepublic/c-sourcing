import urllib.parse


def url_parser(url):
    try:
        # 주어진 URL을 구문 분석
        parsed_url = urllib.parse.urlparse(url)  # URL을 구성하는 여러 부분으로 분해
        query_params = urllib.parse.parse_qs(parsed_url.query)  # 쿼리 문자열을 파싱하여 파라미터 추출
        item_id = query_params.get('id', [''])[0]  # 'id' 파라미터의 값을 추출

        print(item_id)
        return item_id  # 추출된 'id' 값 반환
    except:
        return 'Notfound'  # 예외 발생 시 'Notfound' 반환
    # 이 함수는 URL에서 'id' 파라미터를 추출하여 반환합니다. ->'https://www.example.com/item?id=1234'와 같은 URL에서 '1234'를 추출합니다.
