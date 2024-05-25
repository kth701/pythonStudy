# 딕트셔너리(딕트)
# 키와 값이 쌍으로 저장되는 구조

print("-- dict")
dic = dict(key1=100, key2=200, key3=300)
print(dic)

per = {'name':'홍길동', 'age':15, 'address':'서울시'}
print(per)

# 키 => 값을 호출
print( per['name'], per['age'],per['address'])

per['name'] = '김길동' #수정
print(per)

del per['address'] # 삭제
print(per)

#print('이름:',per['name100']) # 키가 없을 경우
if 'name100' in per:
    print(per['name'])
else :
    print('키가 없음')


# 객체.get(key, "없을 경우 처리할 내용")
name = per.get('name100',"없는 이름입니다.")
print(name)

# 요소 검사
print( 'age' in per) # 키가 존재하면 True, 없으면 False
print( 'job' in per)

print(per)

# 키만 추출
print( per.keys() )
for key in per.keys():
    print(key)

print("---")
# 값만 추출
print(per.values())
for value in per.values():
    print(value)

print("---")

# 키와 값 추출
print(per.items())
for p in per.items():
    print(p)

print("-- 단어 빈도수 구하기 ---")
charset = ['abc','code', 'band', 'band','abc']
wc = {} # []=> 리스트, ()=>튜플, {}=> 딕셔너리, set

for key in charset:
    print("---")
    print(key)

    wc[key] = wc.get(key, 0) + 1
    print("wc[{}]={} ".format(key, wc.get(key,0)))
    

print(wc)

print("-- 자료구조 복제")
name = ['홍길동','이순신','강감찬']
print("내용보기:",name)
print('name addr:', id(name))

# 객체 대입문 => 주소복사, 기억장소내용을 복사한다는 의미가아님.
print("-- name2 = name : 주소가 동일")
name2 = name
print(id(name), id(name2))

name2[0] = '동길이'
print(name, name2)

# 깊은 복사: 내용복사
import copy
name3 = copy.deepcopy(name)

print("-- name, name : deepcopy()")
print(id(name), id(name3)) # name와 name3주소가 다름
print(name, name3) # 내용은 동일함.

name3[0] = '강감찬'
print(name, name3)



