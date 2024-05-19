
# 파일 시스템
import os

# 현재 작업 디렉토리(폴더) 경로 확인
print("현재 폴더: ", os.getcwd() )


# 디렉토리(폴더) 변경
# os.chdir('ex03')
# print("변경후 폴더: ", os.getcwd() )

# print("폴더에 있는 파일정보:")
# print(os.listdir('.'))

# 디렉토리 생성
# os.mkdir('test')
# print("폴더 생성후 정보:")
# print(os.listdir('.'))

# 여러 디렉토리 생성
# os.makedirs('data/image')
# print("폴더 2개이상 생성 후 정보:")
# print(os.listdir('.'))

# 디렉토리 삭제
# os.rmdir('data')
# print("폴더 삭제 후 정보:")
# print(os.listdir('.'))

# 여러개의 디렉토리 삭제
# os.removedirs('data/image')
# print("폴더 삭제 후 정보:")
# print(os.listdir('.'))

