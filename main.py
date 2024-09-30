my_dict = {'Svetlana' : 1987, 'Roma' : 1991, 'Tamara' : 1995}
print (my_dict)
print (my_dict['Svetlana'])
print (my_dict.get('Rimma'))
my_dict.update ({'Alex' : 1985,'Dasha' : 1986})
date = my_dict.pop ('Roma')
print (date)
print (my_dict)

my_set = {1, 2, 'apple', 3, 'd', 1, 'apple', 'd'}
print (my_set)
my_set.add('home')
my_set.add(5)
my_set.discard('d')
print (my_set)