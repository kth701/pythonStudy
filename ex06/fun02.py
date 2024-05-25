# 내장함수
nums = [1,-3,5,4]
print(nums)
print( max(nums), min(nums))
print( sorted(nums,)) # 오름차순
print( sorted(nums, reverse=True)) # 내림차순

#오름차순, key=abs()함수 적용한 요소의 값을 기준으로 정렬
print( sorted(nums, key=abs)) 

# lambda x: x**2 => [1,8,25,16]
print( sorted(nums, key=lambda x: x**2)) # 사용자 정의 함수 (방식: 람다식)

nums2 = [ [5,6],[-30,-10,-10]]
print( max(nums2, key=len)) # list의 개수가 큰 list를 출력
print( max(nums2, key=sum)) # list의 합이 큰 list를 출력

numbers = [1,2,3]
names = ["one","two","three"]
for item in zip(numbers, names):
    print(item)


# 저장소에 있는 값을 추출 
#   : 처음부터 끝까지 순서대로 가져오=> 반복자
for idx, n in  enumerate(numbers,0):
    print("index={},data={}".format(idx, n))

chars = ["*","+","#","&"]
for i, c in enumerate(chars):
    print(i, c, c*i)

#첫번째 인자: 값, 두번째 인자, 판별하고자 하는 자료형(타입)
print( isinstance([1,2,3], list))    

name = "동순이"
age = 10;
print( "내이름은 {}이고, 나이는 {}세입니다.".format(name,age))

#소수점 자리수
num = 1/3
print(num)
print( "num = {:.3f}".format(num))
print( "num = {:10.3f}".format(num))
print( "num = {:010.3f}".format(num))

print( "num = {:d}".format(1000))
print( "num = {:,d}".format(1000))
print( "num = {:10,d} 원".format(1000))
print( "num = {:010,d} 원".format(1000))

#f-string
print(f"{num:,}")


str1 = ["apple","banana","grape"]
print(str1)
print ("/".join(str1))
print ("".join(str1))

print("---")
even2 = []
for i in range(10):
    if (i%2==0):
        even2.append(str(i))

print(even2)

even = [ str(i) for i in range(10) if i%2 == 0]
print(even)








