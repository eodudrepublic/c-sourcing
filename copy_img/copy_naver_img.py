import win32clipboard
import requests
from PIL import Image
from io import BytesIO
import time


def naver_img(img_url):
    print('--------------------------------------\n')

    # 이건 왜 함수 안에 함수가 정의되어 있을까
    # 클립보드에 데이터를 복사하는 내부 함수
    # 이 함수는 바이너리 이미지 데이터를 클립보드 형식에 맞게 변환하여 클립보드에 복사하는 역할을 함
    def send_to_clipboard(clip_type, data):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(clip_type, data)
        win32clipboard.CloseClipboard()

    # 주어진 이미지 URL에서 이미지를 다운로드 -> request.get 요청
    res = requests.get(img_url)

    # 이미지 다운로드 시간 체크
    # print(time.time() - start)

    # 이미지 파일 열기
    request_get_img = Image.open(BytesIO(res.content))

    # 이미지를 BMP 형식으로 변환하고, 바이너리 데이터로 출력
    output = BytesIO()
    request_get_img.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    # print(output)
    output.close()

    # 변환된 이미지 데이터를 클립보드에 복사
    send_to_clipboard(win32clipboard.CF_DIB, data)

    time.sleep(1)  # 짧은 지연시간 추가
    # 이 함수는 웹에서 이미지를 다운로드하고, 이를 클립보드에 복사하는 기능을 수행합니다.
    # 이미지를 클립보드에 복사한 후에는, 해당 이미지를 이용하여 웹사이트에서 직접 이미지 검색을 할 수 있습니다.
