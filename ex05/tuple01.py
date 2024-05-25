# tuple(튜플): list유사, 읽기전용
# 소괄호, 리스트보다 처리속도 빠르다


print("--- list")
list = [1,2,3]
print(list)

list[0] = 100
print(list)


print("--- tuple")
t = (10,)
print(t)

t2 = (1,2,3,4,5)
print(t2)

print(t2[0], t2[1], t2[1:4],t2[-1])
# t2[0] = 100 # error : 튜플은 수정 불가
for i in t2:
    print(i, end="\t")

print()
if 5 in t2 :
   print("있음")
else:
    print("없음")
