# 정규 표현식(Requla Express) : 특정한 규칙을 가진 문자열의 집합을 표현

# 정규 표현식 모듈 : re모듈
# complile(pattern,flags=0) : 패턴을 컴파일하여 Pattern객체 반환
# escape(pattern) : 문자열에서 특수 문자를 이스케이프 처리
# findall(pattern, string, flags=0)
#   : string에서 패턴과 일치하는 모든 문자열을 리스트로 변환
# finditer(pattern, string, flags=0) string에서 패턴과 일치하는 모든 문자열을 반복자로 반환
# ...

# 문자열 찾기
import re   # from re import findall


s = '1234 abc홍길동 ABC_555_6 이사도시'

# 1. 숫자 찾기
print( re.findall('1234', s) )
print( re.findall('[0-9]', s) ) # '[] => or, 0-9사이'
print( re.findall('[0-9]{3}', s) ) # '{n} => n개반복'
print( re.findall('[0-9]{3,}', s) ) # '{n} => n개이상 반복'
print( re.findall('\\d{3,}',s)) # '[0-9]와 "\d" 동일

# 2. 문자 찾기
print( re.findall('[a-z]', s)) # 알파벳 소문자 1자 추출
print( re.findall('[A-Z]', s)) 
print( re.findall('[A-Za-z]', s)) # 영문 알파벳 대소문자 구분없이 1문자 추출
print( re.findall('[가-힣]', s)) # 한글 1자 추출
print( re.findall('[가-힣]{3,}', s))

# 3. 특정 위치의 문자열 찾기
s2 = 'atest tabc 홍길동 1234abc 45test'
print( re.findall('^test',s2)) # ^시작하는문자
print( re.findall('test$',s2))  # 끝나는문자$
print( re.findall('.bc', s2)) # .x or x. 임의의 한문자가 x앞이나 뒤에 오는 패턴

# 단어 찾기
s3 = 'test^홍길동 abc 대한*민국 123$tbc'
words = re.findall('\\w{3,}',s3) # '\w 와 [A-Za-z0-9] 동일'
print( words )

words2 = "".join(re.findall('\\w{3,}',s3))
print(words2)

# 문자열 제외
# print( re.findall('[^^*$]+',s3)) # 'x+' x가 1개이상
# print( re.findall('^test',s3)) # ^x x시작
# print( re.findall('[^test]',s3)) # [^x] x는 제외

