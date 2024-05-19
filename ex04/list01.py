# 자료구조: 프로그래밍에 의해서 만들어진 객체가
# 메모리에 배정될 때 기억공간에 적재되는 구조

# 순서 자료구조, 비순서 자료구조
# 열거형객체: 하나의 메모리영역에 여러개의 자료가 나열
# 열거형객체 - 순서(str, list, tuple), 비순서

# number = 100 # 변수
# name = "홍길순" # 객체

# name2 = str(object='김길동')
# print(name, name2)
# print(type(name), type(name2))
# print(name2[0], name2[1]) # 인덱싱 처리(index)

list1 = [10,20,30,40]
# for n in list1:
#     print(n) 

# for s in name2:
#     print(s)   

# 슬라이싱(범위)     
# print(list1[1:3]) # start index, end index 이전까지
# print('-- [:end index]')
# print(list1[:3]) # 0부터 3이전까지
# print('-- [start index:]')
# print(list1[2:]) # 2이후

# for i in range(1,len(list1)+1): # range(1,5)
#     print(list1[:i]) # 1~4까지 반복

# 리스트 추가,삭제,수정,삽입
# print("= 리스트 추가,삭제,수정,삽입")
# print(list1)

# list1.append(100) # 추가
# print(list1)

# list1[1] = 1000 # 수정
# print(list1)

# list1.insert(0, "길순이") # 삽입
# print(list1)

# list1.remove(100) # 삭제
# print(list1)

# 리스트 연산
# x = [1,2,3,4]
# y = [1.5, 2.5]
# print(x, y)

# print("-- 리스트 결합")
# z = x + y
# print(z)

# z += [10]  #z = z + [10]
# print(z)

# 리스트 확장
# print('-- 리스트 확장: expend()')
# x.extend(['홍길순','동길이','김갑돌'])
# print(x)

# print('-- 리스트 추가')
# x.append(y)
# print(x)

# print('-- 리스트 *연산')
# x2 = x*2
# print(x2)


# x3 = [1,2,3,4,1,2,3,4]
# print('-- 리스트 정렬: sort()')
# print(x3)

# x3.sort()
# print(x3)

# x3.sort(reverse=True) # 내림차순
# print(x3)

# x4 = []
# import random
# for i in range(10):
#     #print(random.randint(1,10),end=" ")

#     rnd = random.randint(1,10) #1-10사이 난수발생
#     x4.append(rnd) # 발생한 난수를 리스트에 추가

# print(x4)

# 리스트 요소 검사
# if 10 in x4 :
#     print("리스트에 포함된 숫자입니다.")
# else:
#     print('리스트에 포함되어 있지 않는 숫자입니다.')
    

# 리스트 내포
x5 =[2,4,1,5,8]
print(x5)

x5_result = []
# for i in x5:
#     #print(i**2) #2**2, 4**2, 1**2, 5**2, 8**2
#     x5_result.append(i**2)

# print(x5_result)


# x5_result = [ i**2 for i in x5]
# print(x5_result)


# 짝수인 값만  2을 곱한 결과
# for i in x5:
#     if i%2 ==  0 :
#         #print(i, i*2)
#         x5_result.append(i*2)

# print(x5_result)

x5_result = [ i*2 for i in x5 if i%2 == 0]
print(x5_result)

#튜플 : 리스트와 유사, '()' 표현,  수정불가
tuble_num = (10,20,30,40,50)
print("-- 튜플")
print(tuble_num, type(tuble_num))
print(tuble_num[0])
print(tuble_num[:3])
print(tuble_num[2:])
print(tuble_num[1:4])

# tuble_num[0] = 100 # error 발생 : tuble 수정불가







# 리스트 연산

