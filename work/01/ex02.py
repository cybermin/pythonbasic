""" 
문자열
"""

data = '안녕하세요.'

#인덱싱
print(data[0])
print(data[-1])

#슬라이싱
print(data[0:2])
print(data[:2])
print(data[4:])

print('='*30)
print('문자열 함수')
print('문자의 길이 : ', len(data))
print('문자의 안녕의 개수 : ', data.count('안녕'))
print('문자의 !이 시작되는 위치 : ', data.find('!'))
#print('문자의 !이 시작되는 위치 : ', data.index('!'))

print(data.replace('안녕', '**') )
#data = data.replace('안녕', '**') 
print(data)

data = '-'.join(data)
print(data)

datasp = data.split('-')
print(datasp)
print(type(datasp))

print('='*30)
#한문자씩 접근
for ch in data : 
    print(ch)