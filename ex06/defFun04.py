# 중첩 함수
# def 외부함수():
#     def 내부함수():
#         처리할 내용
#         처리1...
#         return 값

#     처리2...
#     return 값n

# 일급함수 : 외부함수와 내부함수를 변수에 저장
# 클로저(Function clourse)
#  : 내부함수는 외부함수의 return명령문을 이용하여 반환형태 
# 함수 클로저는 외부함수가 종료되어도 내부함수에서 선언된 변수가 
#   메모리에 소멸되지 않음.

# 데이터
def a1(): # outer 
    print('a1() 함수 실행')
    num = 100*2
    return num # 값(변수) 반환

print("-- 값 반환 ")
n = a1() # n = 200
print(n)

print("--- 외부함수에 내부함수 선언한 식을 반환")
# 함수(식)을 반환
def a(): # outer 
    print('a() 함수 실행')

    def b(): #inner
        print("b() 함수 실행")

    print("a()함수에 b()함수를 실행")
    b()
    return b # 내부함수를 반환

# def b():
#     print("b() 함수 실행")
# b() # b함수 호출

b = a()
print("-- 메인 함수")
b()

# 함수 클로저
print("숫자1~100 리스트에 보관1")
# data1 = []
# for i in range(1, 5):
#     data1 += [i] # 숫자 => 리스트구조 전화 
# print(data1)

data = list(range(1,101))
# print(data)
a = 100
# outer_func = 수행할 명령어
def outer_func(data): # outer function
    dataSet = data # 복사본
    #name = "홍길동"

    # tot(함수형변수) = 함수내용이 들어 있음
    #inner function
    def tot():
        # print(sum([1,2]))
        # print(max([1,2]))
        tot_val = sum(dataSet) # sum() 내장된 함수
        return tot_val # 결과값은 반환
    
    def avg(tot_val):
        avg_val = tot_val/len(dataSet)
        return avg_val
    
    return tot, avg # 함수를 반환

# 함수를 가져옴
tot, avg = outer_func(data)  

tot_val = tot()
print('tot=', tot_val)

avg_val = avg(tot_val)
print('avg=', avg_val)


    



