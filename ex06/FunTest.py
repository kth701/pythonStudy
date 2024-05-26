
# 함수: 독립된 단위 프로그램
a = 1000

# 함수 선언
def forFun():
    name = "홍길동"
    for i in range(1, 6):
        print("Hello !!!")
# 함수 끝
def a():
    print("a")

def b():
    print("b")

def c():
    print("c")


print(a) # 변수 기억장소에 있는 값을 가공
# 함수를 실행 : 명려어를 불러온다.
forFun() # 변수(함수가 가지고 있는 프로그램) 실행
a()
b()
c()

# myPrn() : name, myPrintInner, print()
# myPrintInner: print()
def myPrn(name):
    print("이름:",name)

    def myPrintInner():
        print("myPrinInner() 함수입니다.")
        return name+"님 안녕하세요"

    return myPrintInner # 함수를 반환

n = myPrn("홍길동") # 함수를 수행후 가져오는 값은 함수임.
n()

# 실행 결과 
# def n():
#     print("myPrinInner() 함수입니다.")
#     return name+"님 안녕하세요"
# n()

