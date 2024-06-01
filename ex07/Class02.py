class DatePro:
    constent = "날짜처리 클래스"

    # 생성자
    def __init__(self, year, month, day ):
        self.year = year
        self.month = month
        self.day = day

    # 객체 함수(instance method)
    def display(self):
        print("%d년 %d월 %d일" %(self.year, self.month, self.day))

        print("{}-{}-{}".format(self.year, self.month, self.day))
        print(f"{self.year}년 {self.month}월 {self.day}일")

    # 클래스 함수
    @classmethod 
    def date_string(cls, dateStr):
        year = dateStr[:4]
        month = dateStr[4:6]
        day=dateStr[6:]

        print(f"{year}년 {month}월 {day}")
 

date = DatePro(2024,3,25)

print( date.constent)
print( date.year, date.month, date.day)
# 객체.메소드이름()
date.display()

print("-- 클래스 함수")
#클래스이름.메소드이름()
DatePro.date_string('20240531')

