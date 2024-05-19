# 파일 경로 모듈 가져오기
import os.path

# 현재 경로 확인
print('current path: ',os.getcwd())

# 경로 변경
# os.chdir('./ex03')
# print('change after:',os.getcwd())

# print(os.path.abspath('filepath01.py'))


# 디렉토리 확인
print("디렉토리 유무 확인: isdir()")
print(os.path.isdir('ex04')) # True, False

if (os.path.isdir('./ex04')):
    os.rmdir('ex04')
    print('ex04폴더가 삭제되었습니다.')
else :
    print('ex04폴더가 없습니다.')


# 디렉토리 유무확인
print("디렉토리 유무 확인: exists()")
# print(os.path.exists('ex03'))


# isOK = os.path.exists('ex04') # True, False
# if isOK:
#     print("ex04폴더가 이미 있습니다.")
# else :
#     os.mkdir('./ex04')
#     print('ex04폴더를 생성하였습니다.')


# 파일 유무 확인하기
print("파일 유무: isfile()")
print(os.path.isfile('data/new_text.txt'))
print(os.path.isfile('data/new_text.xml'))
# 파일 사이즈
# print(os.path.getsize('data/new_text.txt'))
fsize = os.path.getsize('data/new_text.txt')
print("파일크기: {}byte".format(fsize))

# 경로 변경
os.chdir('./ex03')
print('current:',os.getcwd())
# 디렉토리 파일 분리하기
print(os.path.split(os.getcwd()))
print(os.path.split('test/hong/abc.txt'))





