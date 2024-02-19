import urllib.parse


def convert_url(first_url):
    try:
        # 주어진 URL을 구문 분석
        parsed_url = urllib.parse.urlparse(first_url)  # URL을 구성하는 여러 부분으로 분해
        path = parsed_url.path  # URL의 경로 부분 추출
        query = parsed_url.query  # URL의 쿼리 문자열 부분 추출

        # URL 경로에서 숫자만 추출하여 상품 ID로 사용
        item_id = ''.join([char for char in path if char.isdigit()])  # 경로에서 숫자만 추출

        # 타오바오 상품 페이지 URL 형식으로 변환
        second_url = 'https://item.taobao.com/item.htm?'
        if item_id:
            second_url += 'id=' + item_id  # 상품 ID 추가
        if query:
            second_url += '&' + query  # 쿼리 문자열 추가

        return second_url  # 변환된 URL 반환
    except:
        return first_url  # 예외 발생 시 원래 URL 반환
