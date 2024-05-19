
# 변수 = 값 : 메모리 상태
# name = "길순이"

# open(파일, 모드, 인코딩)
# 인코딩 생략 = cp949형식
# 윈도우 시스템에서 path구분 기호 "\" => "\\" 인식
# 맥, 리눅스, 유닉스, (윈도우사용가능) 등 시스템에서는 경로 "/"

print("---- .split()")
print("홍길동홍길순동길이")
print("홍길동\n홍길순\n동길이")
print("홍길동\n홍길순\n동길이".split("\n"))

try:
    #  에러발생할 수 있는 부분

    # 파일변수 (파일핸들러)
    file1 = open("data\\text01.txt", "r", encoding="UTF-8")

    # 파일객체.read() : 파일 전체 읽기
    text = file1.read()
    print(text)
    print("---------")
    
    # 파일에 있는 텍스트를 리스트 구조변환
    text_line = text.split("\n") # "\n" 문자기준으로 분리해서 리스트로 저장
    print(text_line) # list구조 : 인덱싱, 슬라이싱[1:3]
    
    print("-- [0],[1]")
    print(text_line[0])
    print(text_line[1])

    print("--- for in ")
    txt2 = [] # 리스트 객체
    
    for txt in text_line:
        txt2.append(txt+"님 안녕하세요!")
        #print(txt)
    print("-- after ")
    print(txt2)



except Exception as e:
    # 에러 처리 하는 부분
    print("Error 발생: ",e)
finally :
    # 에러와 무관하게 무조건 처리
    file1.close() # 자원 해제



