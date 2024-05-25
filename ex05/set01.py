# set() : 중복 제거, 순서가 없다.
# {} : 중괄호

print("-- set")
# 중복 제거: {1,3,5}
s = {1,3,5,3,1,1,1,1,1,3,3,3,3}
print(s)

for d in s:
    print(d, end=" ")
print()
s2 = {3,6}
print(s, s2)

print(s.union(s2)) # 합집합
print(s.difference(s2)) #차집합
print(s.intersection(s2)) # 교집합

s.add(7) # 추가
print(s)
s.discard(3) #삭제
print(s)

# 리스트 -> 중복제거 -> 리스트
gender = ['남','여','남','여']
sgender = set(gender) # list -> set
lgender = list(sgender) #set -> list
print(gender, sgender, lgender)

