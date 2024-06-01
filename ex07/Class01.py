# 클래스 = 멤버변수 + 멤버함수(메서드)
# : 사용자가 정의 자료형 => 타입

# list = [10,20,30]
# print(list)
# print(list[0], list[1:3])

# a = 100

# 클래스 선언(정의)
class myCalc:
    # 클래스 변수: 자료저장
    x = y = 0

    #생성자: 객체생성시 초기값설정
    def __init__(self, a,b):
        self.x = a
        self.y = b

    # 클래스 함수
    def plus(self):
        p = self.x + self.y
        return p

    def minus(self):
        m = self.x -  self.y
        return m


# 객체 = 클래스이름(인자가 값,...)
myObj1 = myCalc(10,20)
# myObj2 = myCalc(1,2)
# myObj3 = myCalc(3,4)

print(myObj1.x, myObj1.y)
print( myObj1.plus() )
print( myObj1.minus() )


# print(myObj2.x, myObj2.y)
# print(myObj3.x, myObj3.y)



        
