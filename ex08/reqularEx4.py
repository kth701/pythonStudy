# 자연어 전처리 예시
# 자연어를 대상으로 토픽분석이나 감성분석 등을 수행을 위해서 
# 전처리 작업수행
# 예) 문장에서 명사만 추출하여 단어의 빈도수 분석, 특수문자,숫자 등 제거

from re import findall, sub

# 텍스트
texts = [
    '우리나라 대한민국, 우리나라%$ 만세',
    '비아그&라 500GRAM 최고!',
    '나는 대한민국 사람',
    '보험료 15000원에 평생 보장 마감 임박',
    '나는 홍길동'
]

print("--------")
print(texts)
print("--------")

# 1. 소문자 변경
texts_re1 = [ t.lower() for t in texts ] 
print("1.단계: 소문자 제거")
print( texts_re1 )

# 2. 숫자 제거
text_re2 =[ sub("[0-9]",'',text) for text in texts_re1]
print("2. 숫자 제거")
print( text_re2 )

# 3. 문장부호 제거
text_re3 = [ sub('[.,?:!;]','', text)  for text in text_re2] 
print("3. 문장부호 제거")
print(text_re3)


# 4. 특수문자 제거 
spec_str = '[@#$%^&*()]'
text_re4 = [ sub(spec_str, '', text) for text in text_re3]
print("4. 특수문자 제거")
print(text_re4)

# 5. 영문자 제거
text_re5 = [ ''.join(findall('[^a-z]',text))  for text in text_re4]
print("5. 영문자 제거")
print(text_re5)

# 6. 공백제거 : 공백기준  splite -> join결합
text_re6 = [ ' '.join(text.split()) for text in text_re5 ]
print("6. 공백 제거")
print( text_re6)
