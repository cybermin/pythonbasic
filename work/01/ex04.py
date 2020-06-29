#부산 3월 기온
temp = [10.8, 8.5, 8.7, 7.9, 5.1, 
        8.1, 8.2, 10.4, 11, 9.9, 
        7.8, 9.5, 11.6, 8.2, 7.7, 
        6.6, 11.1, 12.2, 12.6, 10.4, 
        13.7, 14.1, 12.6, 11.5, 13, 
        14.5, 13.7, 9.4, 10.4, 11.6, 12.9]

print(f'평균기온 : {sum(temp) / len(temp) : 0.2f}')
print(f'최고기온 : {max(temp)}')
print(f'최저기온 : {min(temp)}')

y = [2010,	2011,	2012,	2013,	2014,	2015,	2016,	2017,	2018,	2019]
yavg = [14.9,	14.6,	14.5,	15.3,	15.1,	15.4,	15.7,	15.2,	15.1,	15.7]
ymin = [19,	18.8,	18.6,	19.5,	19.2,	19.5,	19.8,	19.6,	19.2,	19.8]
ymax = [34.1,	33,	34.5,	35,	32.9,	33.5,	37.3,	36.2,	36.4,	35]

'''
for i in range(len(y)) :
    y[i] = str(y[i])
'''

yodd = [item for item in y if item % 2 == 1]
print(yodd)

y = [ str(item) for item in y]
print(y)


ytemp = dict(zip(y, yavg))
print(ytemp)

mintemp = min(ytemp.values())
print(mintemp)

ryear = []
for year, temp in ytemp.items():
    if temp == mintemp :
        ryear.append(year)

for item in ryear : print(item, end = " ")
print()
print('='*30)
y = [2010,	2011,	2012,	2013,	2014,	2015,	2016,	2017,	2018,	2019]
ymax = [34.1,	33,	34.5,	35,	32.9,	33.5,	37.3,	36.2,	36.4,	35]


#1. ymax 최대값
maxv = max(ymax)

#2. 최대값이 있는 위치
ylist = [] 
for i in range(len(ymax)) :
    if ymax[i] == maxv : ylist.append(y[i])


#3. y의 요소 인덱싱
print(ylist)

