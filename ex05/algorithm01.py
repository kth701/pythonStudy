# 최댓값/최솟값
# 정렬 (선택, 버블, 이진,.....)
# 검색 (선형, 이진 ,....)

import random
dataset = [] # 리스트 구조 저장소
for i in range(10):     # 0~9 : 10번 반복 수행
    rnd = random.randint(1,100)
    dataset.append(rnd) # 저장소에 난수를 저장

    #print(i, rnd)

print(dataset)

# 최댓값/최솟값
myMax = dataset[0] # 첫번째 요소 , 최댓값으로 설정
myMin = dataset[0] # 첫번째 요소 , 최솟값으로 설정
for n in dataset:
    if myMax < n:
        myMax = n

    if myMin > n:
        myMin = n
    
print("max=", myMax)
print("min=", myMin)




