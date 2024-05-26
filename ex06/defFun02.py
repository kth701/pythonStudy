
# 1~10까 출력하는 함수 선언

#함수 선언(정의)
def num_count():
    for num in range(1,11):
        print(num)

num_count() # 함수 호출

# 산술 평균
dataset = [2,4,5,6,1,8]
def myAvg(data):
    sum = 0
    for d in data:
        sum += d # sum = sum + d
        # print(d, sum)

    return sum # sum값을 반환


print("-- 산술 평균")
result = myAvg(dataset) #함수 호출
print("합계 : ",result)

# 피카고라스 정의 함수 : a**2 + b**2 = c**2
# 식 : 빗변의 제곱 = 밑변의 제곱+높이의 제곱
def pytha(s,t):
    print("-- 피타코라스의 정의 함수 호출")
    a = s**2 - t**2
    b = 2*s*t
    c = s**2 + t**2
    print("3변의 길이: ", a,b,c)

pytha(2,1)

#함수이름: 함수식별역할, 저장소역할
def mySum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
        #print(i, end=" ")

    return sum

print( mySum(1,10) )
print( mySum(5,10) )
print(  mySum(11,20) )




