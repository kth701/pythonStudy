a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print('/ =>',a/b)
print('// =>', a//b) # 몫
print('% =>',a%b) # 나머지
print('** =>', a**b ) # 승수

#타입 전환(변환)
print(3.5, int(3.5))
print(10, float(10))
print(True, int(True))
print( False, int(False) )
print("10", float("10.5")+100)
print(bool(True),bool(5<2))
print(bool('a'),bool(' '),bool(''))

# 문자열 동일 여부
s = "abcdef"
a = [1,2,3]
print(s[:] is s) # is 판별하는 키워드
print(a[:] is a)

test = [1,2,3] + [3]
print(test)
