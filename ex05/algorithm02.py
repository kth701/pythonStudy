import random

dataset = [] # 리스트 구조 저장소
for i in range(10):     # 0~9 : 10번 반복 수행
    rnd = random.randint(1,100)
    dataset.append(rnd) # 저장소에 난수를 저장

    #print(i, rnd)

print(dataset)

cnt = len(dataset) # 개수  => 10개이면 9번 비교
print("데이터 개수: ", cnt)


# for i in range(5-1): # 0,1,2,3
#     for j in range(i+1,5): # (0,1,2,3),2,3,4
#         print(i,j)

print("정렬전 상태: {}".format(dataset))
for i in range(0, cnt-1): #반복회수 n-1
    for j in range(i+1, cnt):

        if dataset[i] > dataset[j]: # 자리바꿈
            temp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = temp

    print("{}회전 정렬후: {}".format(i+1,dataset))


# print("-----")
# name = "김길동"
# age = 31
# city = "부산001"

# print("--- {}세 ---- {} ---- {}".format(age, name, city))


