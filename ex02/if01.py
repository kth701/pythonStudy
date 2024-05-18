#제어문 : 흐름의방향을 전환
# if 조건식 :
# (띄어쓰기)처리할 내용

#  for

# 단일 조건문 형식
# var = 1
# if var >=5 :
#     print('var=', var)
#     print('조건이 참인경우만 실행')
# print('다음 문장')

# if sum([1,2,30]) > 10 :
#     print([1,2,30])
#     print("sum=", sum([1,2,30]))
# print("out of if")

# 0을 제외한 모든 숫자 True
# if 3:
#     print("three")

# 문자가 있으면 True, 없으면 False
# if "string" :
#     print("string")

# 빈리스트 이면 False
# if [1,2,3] : #True
#     print('list')
# if [] : # False
#     print('[]') 

# if True :
#     print('참')  

# if 'j' in "cat.jpg" :
#     print('j가 포함되어 있음')

# score = 80
# if score >= 60 :
#     if score % 2 == 0:
#         print('60이상이고, 2의 배수')

# if else 문
# num = -10
# if num > 0: #Truee
#     print('0보다 크다')
# else : # False
#     print('0보다 작거나 같다')

#키보드 입력값은 문자열 => 숫자형 전환
# score1 = int(input('점수 입력: '))

# if score1 >=85 and score1 <= 100 :
#     print('우수')
# else : # 85미만인 경우 처리
#     if score1 >= 70: # 70이상
#         print('보통')
#     else : #70미만
#         print('저조')

# print("end if")    

#100~90:A,89~80:B, 70~79:C, 60~69:D, 60미만:F

# score2 = int(input('점수:'))

# if score2>=90 :
#     print('A')
# else : #90미만 
#     if score2 >= 80 : #80이상
#         print('B')
#     else : #80미만
#         if score2 >=70 : #70이상
#             print('C')
#         else : #70미만
#             if score2 >=60 : #60이상
#                 print('D')
#             else : #60미만50
#                 print('F')

# if score2 >= 90:
#     print('A')
# elif score2 >= 80:
#     print('B')
# elif score2 >= 70:
#     print('C')
# elif score2 >= 60:
#     print('D')
# else:
#     print('F')

name = "python"
if name[0] == "p" or len(name) == 6 and "X" in name :
    print("name={}".format(name))


a_words = ["ape", "apple", "ant"]
fruits = ["apple","banana","grape"]

word1 = "apple"
word2 = "ant"

if word1 in a_words and word1 in fruits: #결과값: True
    print("work1 is a-fruit")

if word2 in a_words and word2 in fruits: #결과값: False
    print("work2 is a-fruit")

# 삼항 조건문=> 변수 = 참일경우 if 조건문 else 거짓일 경우
num3 = 3
str1 = "홍길동" if num3 >= 5 else "동길이"
print(str1)
 










