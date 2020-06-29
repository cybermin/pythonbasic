""" '''
딕션너리
'''

dt = {'a': 10, 'b' : 20}

print(dt['a'])

#추가
dt['c'] = 100
print(dt)

#수정
dt['c'] = 10
print(dt)

#삭제
# del dt['a']
# dt.pop('c')
# print(dt)

print('='*50)
for item in dt:
    print(item, "=>", dt[item])

keys = list(dt.keys())
print(keys)    
values = list(dt.values())
print(values)     

items = list(dt.items())
print(items)     

for key, value in dt.items():
    print(key, "=>", value)
 """

lst1 = ['y','x','z']
lst2 = [10,20,30]
dt = dict(zip(lst1, lst2))
print(dt)
print('정렬:' , sorted(dt))

for x, y in dt.items() :
    print(x,':', y)

dt1 = list(zip(lst1, lst2))
print(dt1)

for x, y in dt1 :
    print(x,':', y)

