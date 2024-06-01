# 다형성 : 여러가지 형태를 가질 수 있는 형태

class Flight:
    def fly(self):
        print('날다, fly원형 메서드')

class AirPlane(Flight):
    # 부모로 부터 상속받은 fly() 재정의해서 사용
    def fly(self):
        print('비행기가 날다.')

class Bird(Flight):
     # 부모로 부터 상속받은 fly() 재정의해서 사용
    def fly(self):
        print('새가 날다.')

class PaperAirplane(Flight):
    # 부모로 부터 상속받은 fly() 재정의해서 사용
    def fly(self):
        print('종이 비행기가 날다')    


flight = Flight()

air = AirPlane()
bird = Bird()
paper = PaperAirplane()  

flight.fly()
air.fly()
bird.fly()
paper.fly()

flight = air
flight.fly()

flight = bird
flight.fly()

flight = paper
flight.fly()




    
