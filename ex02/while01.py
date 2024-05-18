# while => 조건이 참인 동안 반복
# 반복횟수가 일정하지 않을 경우 사용

# i = 0
# while i<5: #True이면 반복 처리
#     i += 2 # +2,+4,+6,+8
#     print(i) # 2, 4, 6,...

# i = 0
# while True:
#     i += 1
#     print('hello')
#     if i > 3 :
#         break # loop exit 강제로 제어문 탈출

# print('end')
import random
import math

# 0과 1사이 난수 발생시키는 함수
print("-----------")
for i in range(5): #5번 수행
    rnd = random.random() 
    print(rnd, rnd*10, math.floor(rnd*10))
    print("--")
    print(math.floor(rnd*10) + 1) # 0~9사이 난수 발생
    
print("-------")
# cnt = 0
# while True :
#     r = random.random()
#     print(r)
#     if r < 0.01: #난수가 0.01미만 종료
#         break
#     else:
#         cnt += 1
# print('난수 개수=',cnt)


# break : 제어문 강제로 빠져나옴
# continue : 다음 제어문으로 넘김

for i in range(1, 11):
    if i % 3 == 0 :
        #continue
        break
    print(i)
    print("반복 실행중...!!!")


