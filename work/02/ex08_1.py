'''
파일 처리
'''

#파일 열기
fp = open('지역평균기온.txt', 'r', encoding='utf-8')

#파일 읽기
data = fp.readlines()

#파일 닫기
fp.close()

#문자열 처리
print(data)
print(type(data))

temp = []
for line in data:
    line = line.replace('\n','')
    item = line.split(',')
    print(item[0], '=>', item[1])
    temp.append(int(item[1]))
    
print(f'평균기온 : {sum(temp) / len(temp):0.2f}')