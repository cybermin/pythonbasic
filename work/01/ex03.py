'''
리스트
'''

lst = [1,'python',[10,20,30]]
lst0 = lst[0]
lst1 = lst[2]
lst2 = lst[:1] 

print('인덱싱 :' , lst0 , type(lst0))
print('인덱싱 :' , lst1, type(lst1))
print('슬라이싱 :' , lst2, type(lst2))
print("=" * 30)

lst.append('15.5')
lst[-1] = float(lst[-1])

lst.insert(1, 20)
print(lst)

lst.pop()
lst.pop(1)
lst.remove('python')
print(lst)

lst.append(1)
lst.append(1)
lst.append(1)
print(lst)

lst.remove(1)
print(lst)
print("=" * 30)

lst = [2, 5, 3, 1, 5]

print('리스의 요소의 개수 : ' ,  len(lst))
print('리스의 5요소의 개수 : ' ,  lst.count(5))
print('리스의 5요소의 위치 : ' ,  lst.index(5))

lst.reverse()
print('리스트 역정렬 :' , lst)

lst.sort()
print('리스트 정렬 :' , lst)
lst.sort(reverse=True)
print('리스트 역정렬 :' , lst)

for item in lst :
    print(item)
print("=" * 30)

x, y = 10, 20
print(x, y)

tp = (1, 2, 3) 

for item in tp :
    print(item)