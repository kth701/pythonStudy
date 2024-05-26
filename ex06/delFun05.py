# 획득자, 지정자
# getter(): 외부에서 함수내에 있는 변수를 가져올 때
# nonlocal: 함수내에서 외부함수에서 생성된 자료를 수정

def main_func(num) :
    # 선언된 자원은 main_func함수의 자원
    num_val = num 

    def getter():
        return num_val
    
    def setter(value):
        # 내부함수가 외부함수 자료를 수정할 경우
        nonlocal num_val
        num_val = value

    return getter, setter #함수 반환

# 외부 함수 호출
main_getter, main_setter = main_func(100)

print(main_getter())

main_setter(2000)
print(main_getter())