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
x = [1,2,3,4]
y = [1.5, 2.5]
print(x, y)

print("-- 리스트 결합")
z = x + y
print(z)

z += [10]  #z = z + [10]
print(z)








# 리스트 연산

