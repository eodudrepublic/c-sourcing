import csv


def load_banned_words(filename):
    banned_words = []  # 금지된 단어들을 저장할 리스트
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)  # CSV 파일 리더 객체 생성
        for row in reader:
            banned_words.extend(row)  # 각 행에 있는 단어들을 banned_words 리스트에 추가
    return banned_words  # 금지된 단어 리스트 반환
    # 해당 함수는 주어진 파일명의 CSV 파일에서 금지된 단어들을 읽어 리스트로 반환합니다.
    # 예를 들어, 'ban_word.csv' 파일에 금지된 단어들이 쉼표로 구분되어 있을 경우, 이 단어들을 모두 읽어와 리스트에 저장합니다.


def check_words_in_sentence(sentence, banned_words):
    # 주어진 문장에 포함된 금지된 단어들을 찾아 리스트로 만듦
    found_words = [word for word in banned_words if word in sentence]
    return len(found_words)  # 찾은 금지된 단어의 수를 반환
    # 이 함수는 주어진 문장에서 금지된 단어들이 포함되어 있는지 검사하고, 포함된 금지된 단어의 개수를 반환합니다.
