
# open(file, mode, encoding)
# r,w,x,a,b


file = open("data\\text.txt", mode="r", encoding="UTF-8")
# print(file) # 파일에 대한 정보 표시

# text = file.read() # 파일 전체 읽기
# print(text)
# print(type(text)) # string 타입

# textLine = file.readline() # 한줄 읽기
# print(textLine) 
# print(type(textLine)) # string 타입

lines = file.readlines() # 전체를 줄단위 읽기
# print(lines)
# print(type(lines)) # list 타입

cnt = 1
for i in lines: # list구조
    cnt+=1
    print("{}:{}".format(cnt, i))

# 파일 쓰기 
file2 = open("data\\new_text.txt", mode="w", encoding="UTF-8")

file2.write("melon")
file2.write("title")
file2.write("길순이")



