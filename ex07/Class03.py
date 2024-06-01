
class Test:
    num = 100 # 공개형 변수

test = Test() # 클래스 타입으로 객체를 생성
print("공개형 변수 : ",test.num)
test.num = 1000
print("공개형 변수 : ",test.num)


# 캡슐화 : 여러정보를 묶음, 정보은닉
# 공통 인터페이스 : getter(획득자), setter(지정자)

class Account:
    # 멤버변수 : 비공개=> 은닉 => "__변수이름"
    __balance = 0 # 잔액
    __accName = None # 예금주
    __accNo = None # 계좌번호

    def __init__(self, bal, name, no):
        self.__balance = bal    # 잔액 초기화
        self.__accName = name     # 예금주 초기화
        self.__accNo = no       # 계좌번호 초기화

    # 인스턴스 함수 통해서 접근
    # 계좌 정보 확인
    def getBalance(self):
        return self.__balance, self.__accName, self.__accNo

    # 입금하기
    def deposit(self, money):
        self.__balance += money # a = a + 10 => a+= 10

    # 출금하기
    def withdraw(self, money):
        if self.__balance < money:
            print('잔액 부족')
            return # 함수를 종료
        
        self.__balance -= money


acc = Account(1000, '홍길동','123-123-1234-12')
# print(  acc.__balance )# 접근 에러 발생
bal = acc.getBalance()
print("계좌정보: ",bal)

# 입금 처리
money = int(input('입금금액:'))
acc.deposit(money)
bal = acc.getBalance()
print("계좌정보: ",bal)

# 출금 처리
money = int(input('출금금액:'))
acc.withdraw(money)
bal = acc.getBalance()
print("계좌정보: ",bal)


