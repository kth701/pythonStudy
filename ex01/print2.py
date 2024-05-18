# 문자열 : "" or ''

name = "홍길동"
addr = '부산' +'진구'
print(name, addr)
print('이름:'+name)

print(type(100))
print(type(10.5))
print(type('나이'))

print('bool->',10<2) # True/False
re = True # true
print(re,type(re))

a,b = 100,200 # 동시대입, 분할할당
print(a,b)

str = "홍길동\t홍길순\n강감찬"
print(str)
str1 = '''
동순이
   길순이
        강감찬'''
print(str1)
# 변수 : 단일기억장소
n1 = 100
print(n1)
n1 = 200
print(n1)
# 숫자 발생
n2 = 0
n2 = n2+1 # 0 + 1
print(n2) # 1

n2 = n2+1 # (0+1) + 1
print(n2) # 2

n2 = n2+1 # (0+1+1) + 1
print(n2)

num3 = [10,20,30,40]
print(num3[3])

#문자열 : 부분추출
# [시작번호: 끝번호 : 증가]
fName = "test.py"
print("-----")
print(fName)
print(fName[6])
print(fName[0:3]) #tes
print(fName[0:])
print(fName[:3])
print(fName[-1]) # 오른쪽->왼쪽
print(fName[-3:-1])
print(fName[0:-1:2]) # 
