# 함수 장식자: 데코코레이터(decorator)

def wrapHello(func): # func변수 = hello()함수 주소
    def resultHello():
        print('방가워요!!!')
        func() # hello()
        print('잘가요!!!')

    return resultHello

@wrapHello
def hello():
    print("hi~~~~ ","홍길동")

hello()

print("----")

def decoHi(f): # 기존함수 주소 전달
    def new_f(): #기능추가
        print("f() is called") 
        return f() # f(): 기존함수를 수행한 결과를 반환 => hi()
    
    return new_f # 함수의 주소를 반환한다.


@decoHi
def hi():
    print("hi")

hi()



def func_double(f):
    def new_func(x):
        y = f(x) # double(x) = 2*x
        print(y)
        return y
    
    return new_func


@func_double
def double(x):
    return 2*x

print( double(5))