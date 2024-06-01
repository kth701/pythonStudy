# 함수 : 기능 => 명령어의 집합
# 독립된 단위 프로그램


# print("---")
# def userFun():
#     print('hello!!!')
#     print('파이썬!!!')

# # 함수 실행(호출)
# userFun()

# def userFun01(mes):
#     print( '전달받은값:',mes)

# # 함수 실행(호출) : 데이터 전달
# userFun01('홍길동')
# userFun01('hong')

# def userFun02(a,b):
#     print(a,b)
#     print('add=', a+b)
#     return (a+b) # 값을 반환

# # 함수 실행(호출) : 값전달, 결과값 가져오기
# #add = userFun02(10,20)
# print( userFun02(10,20) )

# def userFun03(a,b):
#     a1 = a+b
#     a2 = a*b
#     a3 = a/b
#     a4 = a-b
#     return a1,a2,a3,a4

# r1,r2,r3,r4 = userFun03(10,3)
# print(r1,r2,r3,r4)


# def userFun04(*num):
#     print(num)
#     for i in num:
#         print(i, i*2)

# # 함수 실행(호출) : 데이터 전달 개수 제한이 없음.
# userFun04(1,2,3,4)

# def userFun05(*nums, **maps):
#     print("nums={}".format(nums))
#     print("maps={}".format(maps))

# userFun05(10,20,30, name="홍길동", age=30)

# # 중첩 함수 => 
# # 일급함수:외부함수에서 내부함수를 호출하면 내부함수가 반환

# def a():
#     # outer Function
#     print('a() 함수 호출됨.')

#     def b(): # inner Function 정의(선언)
#         print('a()안에 있는 b()함수 호출됨.')

#     # a()함수에 b()함수를 호출
#     return b # 내부함수 b()함수 주소를 반환

# print("-- 일급함수 : 외부함수에서 내부함수 가져오기")
# main_b = a() # a()함수 호출 => b함수를 가져오기
# main_b() # b()함수를 호출(실행)

# 재귀함수 : 자기자신을 호출
# 끝내기 조건이 반드시 있어야함.
def Counter(n):
    print(n)

    if n==0:
        return 0
    else :
        return n+Counter(n-1)
        # 3 + (2) + (1) + 0

print("-- 재귀함수")
sum = Counter(10)
print("---")
print(sum)






