name = "variable"
print(name)

# input() : 키보드로 입력받은 문자열
# myName=input("이름입력:")
# print("이름:"+myName)


# 문자열 + 문자열 => 연결된 문자열
# 문자열 + 숫자형 => 타입에러
# score = float(  input("점수입력:") )
# print( score + 10)

# 학생이름, 국어,영어,수학점수를입력받아
# 총점,평균 구하기

name = input('이름:')
kor = float( input('국어:') )
eng = float( input('영어:') )
mat = float( input('수학:'))

tot = (kor+eng+mat)
avg = tot/3
print('총점', tot)
print('평균', avg)
