# 지방, 탄수화물, 단백질 칼로리의 합계를 계산

# 처리 조건

# 1. 지방, 탄수화물, 단백질의 그램을 키보드로 입력
# 2. 총 칼로리 = 지방*9+단백질*4+탄수화물*4

# 출력화면

# 지방의 그램: 25
# 탄수화물 그램: 520
# 단백질 그램: 45
# 총칼로리: 2485 cal

# 키보드로 입력된 데이터 => 문자열=> 타입전환
fat = int( input('지방의 그램') )
carb = int( input('탄수화물 그램'))
pro = int( input('단백질의 그램'))

tot = fat*9 + pro*4 + carb*4
print('총 칼로리:', format(tot,'3,d'), 'cal')