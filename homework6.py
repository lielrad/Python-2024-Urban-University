my_dect = {'Don': 1986, 'Mary': 2002, 'David': 1998}
print(my_dect)
print(my_dect['Don'])
print(my_dect.get('Tom'))
my_dect.update({'Tom': 2015, 'Lisa': 1973})
print(my_dect['Mary'])
del my_dect['Mary']
print(my_dect)

my_set = {1,2,'box',False,'pen',(1,2,3),'box',(1,2,3),3,1,2,3}
print(my_set)
print(my_set.add(4))
print(my_set.add('day'))
print(my_set.discard(1))
print(my_set)