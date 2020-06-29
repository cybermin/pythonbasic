'''
파이썬 입출력 프로그램
'''
# 입력
# 데이터 타입 변환 : int() , float(), str()
x = int(input('숫자를 입력하세요.'))
y = int(input('숫자를 입력하세요.'))

#출력
print(str(x) + '+' + str(y) + '=')
print(x , '+' , y , end=' = ')
print(x+y)

print('-'*50)
print(f'{x} + {y}  = {x+y}')
print(f'{x} - {y}  = {x-y}')
print(f'{x} x {y}  = {x*y}')
print(f'{x} ^ {y}  = {x**y}')
print(f'{x} / {y}  = {x/y:.2}')
print(f'{x} // {y}  = {x//y}')
print(f'{x} % {y}  = {x%y}')





