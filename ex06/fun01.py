# 모듈과 패키지 : 파이선에 제공하는 라이브러리
# 모듈 : 다수의 함수와 클래스 묶어서 *.py
# 패키지 : 비슷한 유형의 모듈

# 내장함수 : import하지 않고 바로 사용
# builtins모듈 => print(), abs(x), bool(x), dict(), dir(),...

# import 모듈명 : 모듈에 있는 모든 함수를 가져오기
# from 모듈명 import 함수명1,... : 모듈에 필요한 함수만 가져오기

print("Hello")

# all() => && (and) : 모든 요소 True=> True
print(   all([1, True, 10, -15.2, 0])  )

# any() => || (or) : 요소중 하나라도 True => True
print( any([1,10,0,-10])  )
print( any([0,0,"",[]])  )
print(4, bin(4)) # 2진
print(10, hex(10)) # 16진
print(10, oct(10)) #8진
print( eval("10+20"))
print( 'A', ord('A'))
print( 'a', ord('a'))

l = zip( [1,3,5], [2,4,6])

print(l, list(l))


