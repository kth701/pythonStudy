# ** -> *,/,//,% -> +,-
# print( 2+3*2**2 )
# print("10"+"A"*3)

# 리스트 구조: '+' 추가를 의미
# nums = [0,1]+[2]*3
# print(nums)

# 나누기: 
#'/'=> 소수점 이하 계산 '//' => 몫, '%'=> 나머지
# print(type(7/2),  type(7//2),  7%2 )

# 주의
# print(7/0)
#print(5.0**1000) # 5의 1000승 : 숫자범위 벗어남 에러
#print(5**1000) # 정수는 가능

# 비교연산자 : True/False
# print(10 == 10) # True
# print(10 != 10) # False
# print(10 < 3) # False
# print(10 >= 3) # True

# a = 10
# print( a, a==10)
# print(5 == 5.0)

# 문자열 비교
# print("---")
# print("A"<"B") #65 < 66
# print("A">"B") # 65 > 66
# print("A"=="B") # 65 == 66

#멤버 연산자 : 문자 포함여부
# in , not in
# print("-- in, not in")

# s = "ABCDE"
# print( "A" in s)
# print( "F" in s)

# nums1 = [1,2,3]
# print( 1 in nums1) # True
# print( 10 in nums1) # False
# print( 4 in [1,2,3,4]) # True

# 논리연산자
# print("-- 논리연산: not and or ")
# and 모든조건결과 True => True
# print( 5>2 and 5>3 and 5>1) # True
# print( 5>2 and 5>3 and 5<1) # False

# or 모든 조건 결과 False => False
# print(5<2 or 5<3 or 5>1)
# print(5>2 , not 5>2 )

# s2 = "python"
# print( ("py" in s2) and ("thon" in s2) )

# 대입연산자
num1 = 10
# num1 += 10    # num1 = num1 + 1
# num1 += 10
# num1 += 10
# print(num1)#13

num1 -= 3 # 10->7
print(num1) #10
num1 *=2 # 7 -> 14
print(num1)



