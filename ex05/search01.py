# 검색 (선행: 처음부터 순차적으로 비교하여 검색)


dataset = [10,20,30,90,80,-20] # 리스트 구조 저장소
print(dataset)


data = 80
for i in range(len(dataset)):
    if dataset[i] == data: # dataset[0], dataset[1],...
        print(i+1,"번째에 있음. ")

