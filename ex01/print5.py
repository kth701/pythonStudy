# 함수: 내장함수 => 이미 많들어 놓은 기능
print( '절대값:',abs(10),abs(-10) )
print("반올림:", round(3.5), round(3.2), round(12.7568,2))
print("문자열길이:", len("abcd") )

str = "홍길동홍길순"
num1 = [10,20,30] # 여러개의 기억장소
print( len(str), len(num1))

# 합계
print("합계:", sum( [1,2,3] )   )
print( sum(num1), sum( num1,100) )

# 최대,최소
num2 = [1,100,50,20]
print('최대:', max(num2))
print('최소:', min(num2))

word = ["apple","orange","grape"]
print(max(word), min(word))
# "apple"       => 첫번째 문자 비교, 두번째 문자 비교,,
# "orange"
# "grape"

# 정렬: 오름차순(asc), 내림차순(des)
num3 = [10,20,-30,-100,1,2,3]
print( sorted(num3))
print( sorted(num3,reverse=True ))
str3 = ["apple","orange","grape"]
print( sorted(str3) )

# 특정기준 정렬
print( sorted(num3, key=abs, reverse=True))

# 에러 발생
# print(len(5)) # 에러(리스트구조에만 적용)
# print( len(1,2,3)) #에러 (인자개수 타입에러)
# print( sum([   [1,2],  [3,4]  ]) )