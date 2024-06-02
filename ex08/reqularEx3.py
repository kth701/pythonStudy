# re.splite(p,str,x,y) : string을 대상으로 패턴과 일치하는 문자열을 
# 분할하여 부분 문자열이 포함된 리스트 반환

# 올바른 문장 선택 예시
from re import split, match, compile

# 테스트 자료
test = "홍길동\n홍길순"
print( test )

multi_line = """http://www.naver.com
www.hongkildong.com
www.daum.net
http://www.google.com
"""
print( multi_line )

# 1. 구분자를 이용하여 문자열 분리
web_site = split("\n", multi_line)
print(web_site)

# 패턴 객체 생성
pat = compile("http://")

# 패턴 객체를 이용하여 정상 웹 주소 선택
sel_site = [ site for site in web_site if match(pat, site)  ]
print(sel_site)

# 