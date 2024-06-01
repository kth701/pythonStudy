class C:
    def __call__(self, num):
        return num*2
    def in_num(self, a,b):
        return a+b
    
inst = C()
# num = inst.__call__(1000) 
num = inst(100)
print(num)
print("---")

class C2:
    def __init__(self, attr):
        self.attr = attr
    
    def __len__(self):
        return self.attr
    
num2 = C2(100)
len_num2 = len(num2)   

print("---")
class C3:
    def __init__(self, attr):
        self.attr = attr
    
    def __getitem__ (self, idx):
        return self.attr
    
num3 = C3([10,20,30])
len_num3 = num3[100]
print(len_num3)

print("---")
class FindPath:
    def find(self, start, end):
        print(start, end)

class FPBicycle(FindPath):
    def get_bicycle_road(self, s, e):
        super().find(s, e)
        print("get bicycle..")

# 부모 클래스 : 기능 축소
# 자식 클래스 : 기능 확대

bicycle = FPBicycle()

# bicycle.find("서울", "부산")
# bicycle.get_bicycle_road()

bicycle.get_bicycle_road("서울","부산")

print("---")
class C4:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    
c4 = C4(10, 20)
print( c4.x) 

# c4.x(100)
c4.x = 100
print( c4.x)