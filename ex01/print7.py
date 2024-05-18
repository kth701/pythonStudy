# %d(10진 정수), %x(16진), %o(8진)
# %f(실수형), %s(문자열),%c(단일문자) 

print("----")
print( "%d" %(1000) )
print( "%10d" %(1000))
print( "%x" %(15))
print( "%o" %(8))

print( "%f" %(3.14159))
print( "%.2f" %(3.14159))
print( "%8.2f" %(3.14159))
print( "%s %c" %("길순이", 'c'))
print("----")

name = "홍길동"
age = 20
data = 3.14159
# print("%양식문자" %(값))
print("이름: %s, 나이: %d, data=%.2f" %(name, 10, 10.2) )

str_frm = f"이름: {name}, 나이 {age}"
print(str_frm)

#문자열 관련 함수
s ="It is Python!"
print(s.upper()) #대문자전환
print(s.lower()) #소문자전환

# 문자열 분리해서 리스트구조 변환
s_list = s.split()
print(s_list)
print( "orage, apple, grape".split(',') )

formula = "x+y+z=12"
left =formula.split("=")
print(left, left[0], left[1])

vars = left[0].split("+")
print(vars)

str = "     abc     " # 5빈칸+3+5빈칸
print( len(str))
print( len(str.lstrip())) #왼쪽 공백 제거
print( len(str.rstrip())) #오른쪽 공백 제거
print( len(str.strip())) #양쪽 공백 제거

s2 ="It is Python!"
s3 = s2.split()

print(s3)
print('-'.join(s3))

str4 = [3,2,1]
print(str4)

str4.append(100)
print(str4)
str4.append([1000,2000])
print(str4)

temp = str4.pop() #제거하고 반환
print(str4)
print(temp)

str4.pop(1)# 인덱스1번에 위치한 내용 제거
print(str4)

str4.remove(1) # 제거항목을 반환하지 않는다.
print(str4)

str5 = ["orage", "apple", "grape"]
idx = str5.index("apple") # 입력요소의 위치
print(idx)

