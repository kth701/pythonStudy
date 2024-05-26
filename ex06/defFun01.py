# 사용자 정의 함수
# 독립된 단위 프로그램

# 함수 선언


# 1. 인자가 없고, 반환 없는 형식
def userFunc():
    print('-- 인수가 없는 함수')
    print("userFunc1 호출되었습니다.")

# 함수 호출(실행)
userFunc()

# 2. 인자가 있고, 반환 없는 형식
# 함수 내에서 선언된 변수: 지역변수
def userFunc2(x,y): # 매개변수: 전달 받은 값을 저장하는 변수
    print('-- 인자가 있는 함수 호출')
    print('전달받은 값:',x,y)
    z = x + y
    print(z)

userFunc2(100,20)

# 3. 인자가 있고, 반환 있는 형식
def userFun3(x,y):
    print('-- 인자가 있고, 반환 값이 있는 함수 호출')
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y 

    return add, sub, mul, div

# 키보드로 데이터 입력
a = int(input('x: 입력: ')) # 키보드(str -> int)
b = int(input('y: 입력: '))

n1, n2, n3, n4 = userFun3(a, b)
print("더하기: ", n1)
print("빼기: ",n2)
print("곱하기: ",n3)
print("나누기: ", n4)




