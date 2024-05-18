# for 변수 in 저장소:
#     반복 처리할 내용

print("-- for in")
str1 = "apple"
for s in str1:
    print(s, end=", ")

print("")
for n in [10,20,30]:
    print(n*2, end=" ")

# 반복 횟수(range)
print("-- for  range")
for i in range(10): #0~9숫자를 생성하여 반복 처리
    print(i+1, end=" ")

print('--  for range(start, end)')
# sum = 0
# for i in range(1,11):
#     sum += i  # +1, +2,.. +10
#     print("1~{} : {}".format(i, sum))


# dan = int(input('단을 입력하세요: '))
# for i in range(1,10) : # 1~10
#     #print(dan,i, dan*i)
#     print("{} x {} = {}".format(dan, i, dan*i))

# 다중 for
# for i in range(2,10): # 2~9 단 숫자 발생
#     print(" {} 단".format(i))
#     for j in range(1,10): # 1~9 곱 숫자 발생
#          print("{} x {} = {}".format(i, j, i*j))

files = [
    "apple.jpg",
    "banana.png",
    "names.txt",
    "grape.jpg",
    "profiles.text"]
jpgs = []

for f in files:
    if f[-4:] =='.jpg': #확장자가 .jpg문자열만 추출
        print(f,[f])
        jpgs += [f] # ["apple.jpg"]

print(jpgs)


#리스트 구조 '+'연산자 : 추가(병합)
# list1 = [1,2]
# list2 = [3]
# list3 = list1+list2 #[1]+[2]

# list4 = [1]
# list4 += [2] # list4 + [2]
# list4 += [3] # list4 + [3]
# list4 += ["test.py"]

# print(list1)
# print(list2)
# print(list3)
# print(list4)


words = ["app", "monkey", "gorilla"]
for w in words:
    # print(w)
    if len(w) > 5 :
        print(w)

print("-- 이중 List")
num_lists = [ 
    [10,20], # 0행-> 0열, 1열
    [100,200] # 1행 -> 0열, 1열
]
print(num_lists)
print(num_lists[0], num_lists[1])
print(num_lists[0][0],num_lists[0][1])

print("-- 이중 List , 다중 for")
for row in num_lists:
    print("---")
    print(row)
    for col in row : 
        print(col)

string = """나는 홍길동 입니다.
주소는 부산시 입니다.
나이는 15세 입니다."""

sents = [] # 문장 저장소
words = [] # 단어 저장소

print( string.split(sep="\n") )
temp1 = string.split(sep="\n")

for sen in temp1:# '\n'기준으로 분리하여 list구조 저장
    sents.append(sen)

    # 문장 -> 단어
    for s in sen.split():
        words.append(s)

print("문장:",sents)
print("문장수:", len(sents))
print("단어:", words)
print("단어수:",len(words))

