# re 모듈관련 함수 가져오기
from re import findall, sub


# 텍스트 처리
texts = [
    '우리나라 대한민국, 우리나라%$ 만세',
    '비아그&라 500GRAM 최고!',
    '나는 대한민국 사람',
    '보험료 15000원에 평생 보장 마감 임박',
    '나는 홍길동'
]

# 텍스트 처리하는 함수 정의
def crean_text(text): # 처리할 문자 전달 받음
    # 1-6단계
    texts_re = text.lower() # 소문자로 전환
    texts_re2 = sub("[0-9]",'',texts_re) # 숫자 제거
    texts_re3 = sub('[.,?:!;]','', texts_re2) # 문장부호 제거
    texts_re4 = sub('[@#$%^&*()]', '', texts_re3) # 특수문자 제거
    texts_re5 = ''.join(findall('[^a-z]',texts_re4))
    texts_re6 = ' '.join(texts_re5.split()) # white space 제거

    return texts_re6

# 함수 호출(실행)
texts_result = [ crean_text(text) for text in texts]

print("-----")
print(texts)
print("-----")
print(texts_result)
