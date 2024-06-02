import ex09.myPackage.scaterring

data = [1,3, 1.5, 2, 1, 3.2]

# 산술 평균 함수 호출
print('평균: ', ex09.myPackage.scaterring.Avg(data))


# 2. 모듈 추가
from ex09.myPackage.scaterring import Avg, var_sd
print('평균: ', Avg(data))
var, sd = var_sd(data)
print('분산 : ',var)
print('표준편차: ',sd)