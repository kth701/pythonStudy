# 지역변수, 전역변수
# 전역변수 : 모듈 내에서 접근 가능
# 지역변수 : 함수 내에서만 접근 가능

num1 = 100 #변수선언
print("함수 밖에 선언한 변수:",num1) # 전역 변수 

def a():
    num2 = 200 #지역변수
    num1 = "홍길동" # 지역변수 선언
    print("함수안에 있는 지역변수:",num2)
    # print("함수 안에 선언한 변수:",num1)

    # global num1  # 전역변수 지칭
    # print("함수 밖에 선언한 변수(global):",num1)


a() #함수 호출
print(num1)

#print(num2) # error 발생

# 함수에 인자값을 전달할 경우 : 가변인자=> "*매개변수"
# 가변인자 : 인자의 개수에 상관없이 입력을 받을 경우
def Func1(score,name, *arg):
    print("-- 가변인자 값")
    # print(arg) #튜플

    print(score, name)
    for i in arg:
        print(i)


# Func1(100,200,300)
# Func1(1)
Func1(100,"홍길동",True, "길순이")


# "**매개변수": 사전형자료(딕셔너리)를 받는 가변인자
def emp_func(name, age, **other):
    print(name)
    print(age)
    print(other)

emp_func('홍길동',10, address='부산', height=17)    

print("---")
def group_by_age(**kwargs):
    # 지역변수 
    # 딕셔너리 타입=> {key:value,...}
    # 객체['키'], 객체.get(키), 객체.get(키,대체할 값)
    group = {"adult":[], "non-adult":[]}

    # 딕셔너리객체.values(), 딕셔너리객체.keys(), 딕셔너리객체.items()
    print(kwargs)
    for name, age in kwargs.items():
        # print(name, age)
        if age > 18:
            print(name, age)
            print("19이상")
            # 리스트 연산 : '+ ' 추가
            # [10,20]+[100] => [10,20,100]

            # group["adult"] = group["adult"] +[name]
            group["adult"] += [name]
        else :
            print(name, age)
            print("19미만")
            group["non-adult"] += [name]

        #print(group)

    return group

reusult = group_by_age( kim=25, jeong=16, hong=20, sun=10)

print(reusult)

print("-- ")
def Func3(*a, **b):
    print("a = {}".format(a))
    print("b = {}".format(b))

Func3()
Func3(1,2)
Func3(first="홍길동", second="길순이")
Func3(10,20,30, addr="부산",age=10)

def myFun(name:str, age:int) -> int:
    print(name, age)
    return 100

num = myFun("홍길동", 10)
print(num)

# 함수 선언 : 명시적인 함수 선언
# 람다 함수 : 익명함수, 함수를 인자로 사용할 경우
# 함수이름(데이터, 리스트, 튜플, 딕셔너리,...)

# 일반 함수
def Add(x,y):
    return x + y

print("-- 일반함수")
print('add = ', Add(10,20))


# 람다 함수
print("-- lambda function")
print( 'lamda add=', (lambda x,y: x+y )(100,20)   )

# 변수 = 함수식(함수 본체)
eq = lambda a,b,c : "{}x + {}y = {}".format(a,b,c)
print(eq(5,4,3))

# 일반 함수
def eqFun(a,b,c):
    return "{}x + {}y = {}".format(a,b,c)

print(eqFun(5,4,3))

print("-- 형식 있는 출력")
# 단순(값만) 출력
a1=100
b1=200
c1=300
print(a1,b1,c1)
# 형식을 갖춘 출력
print("a={},b={},c={}".format(10,20,30))






