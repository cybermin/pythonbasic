'''
집합 : {}
'''
lst = [1,2,2,3,3]
st = set(lst)
lst = list(st)

print(type(lst))
print(type(st))
print(st) 
print(lst) 

st2 = {3, 4, 5}
print('교집합 : ', st & st2) 
print('합집합 : ', st | st2) 
print('차집합 : ', st - st2) 

lst = [5,2,1,10]

print(sorted(lst))
print(lst)

lst.sort()
print(lst)