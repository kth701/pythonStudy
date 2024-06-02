# 라이브러리 import(가져오기)
# 1. import 모듈 => 파이썬에서는 프로그램의파일.py
#                => 패키지 : 모듈을 묶음(폴더:경로)
# 2. import 패키지.모듈 # 패키지에 포함된 모듈
# 3. from 패키지.모듈 import 함수, 클래스,... 

# 평균과 제곱근 모듈 import
from statistics import mean
from math import sqrt

# 산술 평균 함수 정의
def Avg(data):
    avg = mean(data)
    return avg

# 분산/표준편차 함수 정의
def var_sd(data):
    avg = Avg(data) # 산술평균 함수 호출(실행)
    diff = [ ( d-avg)**2   for d in data]
    var = sum(diff) / (len(data)-1) # 분산 
    sd = sqrt(var) # 표준편차

    return var, sd


if __name__ == "__main__":
    data = [1,3, 5, 7]
    print('평균: ', Avg(data))

    