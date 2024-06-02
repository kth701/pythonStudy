# 문자열 검사 : re.match  호출

# from re import match

# 패턴과 일치 여부 판별
# jumin = '123456-1234567'
# jumin = input('주민번호 입력하세요.')
# result = match('[0-9]{6}-[1-4][0-9]{6}', jumin)

# print( result )
# if result:
#     print('주민 번호가 정상 처리')
# else :
#     print('잘못된 주민번호')

# 문자열 치환 : re.sub 호출
# from re import sub
import re

str = 'test^홍길$$$동 abc *test 대한*민국 123$tbc'

# 특수문자 제거 re.sub(패턴, 바꾸어질 문자, 대상문자열)
text1 = re.sub('[\^*$]+', '',str) # '^*$+ => *와 $문자가 1개이상

print( str)
print(text1)

# 숫자 제거
text2 = re.sub('[0-9]','', text1)
print(text2)

