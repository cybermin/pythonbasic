'''
BMI = 체중(kg) / (키(m) x키(m))
'''

weight = float(input('몸무게 (kg) :'))
height = float(input('키 (cm) : ')) / 100

BMI = weight / height**2

print(f'몸무게 {weight}kg, 키 {height*100}cm  => BMI : {BMI:0.2f} ')
