# 부모 클래스
class SuperClass:
    # 생성자 -> 멤버변수(속성)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 함수(메서드)
    def display(self): #멤버 변수 출력
        print(f"name : {self.name}, age: {self.age} ")

# 객체 생성
sup = SuperClass("부모클래스", 50)
sup.display()

# 자식 클래스(상속받을 부모클래스이름)
class SubClass(SuperClass):
    gender = None

    def __init__(self, name, age, gender):
        # super : 상위 클래스 (부모)
        # 부모 생성자 호출하여 부모객체변수값을 초기화 작업
        super().__init__(name, age)
        self.gender = gender # 자식 클래스 변수

    # 함수 : 재정의 (오버라이딩)
    def display(self):
        print("---")
        super().display() # 부모 클래스 함수 호출
        print("---")
        print(f"이름: {self.name}, 나이: {self.age}, 성별: {self.gender}")


sub = SubClass('자식클래스', 25,'여자')
sub.display()


