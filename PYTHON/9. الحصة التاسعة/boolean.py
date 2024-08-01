print(bool('dsgjdskfm'))
print(bool(-1))
print(bool(1.13465))
print(bool([13,'dgvsd' , 24.24]))
print(bool((13,'dgvsd' , 24.24)))
print(bool({13,'dgvsd' , 24.24}))
print(bool({13:'dgvs'}))

#---------------------
print('-'*50)

print(bool(''))
print(bool(0))
print(bool(0.00000000000))
print(bool([]))
print(bool(()))
print(bool({}))

#----------------------
print('-' * 50)

print(3>0 and 6==6)
print(3>0 and 6!=6)

print(3>0 or 6!=6)
print(3<0 or 6!=6)

print(7 == 8 or 5 > 2 and 3 < 10)
print(7 == 8 or 5 > 2 and 3 > 10)

print(not (3>0 and 6!=6))

#-----------------------
print('-' * 50)

mystring = 'Jamal'

print('J' in mystring)
print('c' in mystring)

mylist = ['ekfkf' , 75 , True]

print(75 in mylist)
print('jamal' in mylist)

mytuple = ('ekfkf' , 75 , True)

print(75 in mytuple)
print('jamal' in mytuple)

mystring = 'Jamal'

print('J' not in mystring)
print('c' not in mystring)

mylist = ['ekfkf' , 75 , True]

print(75 not in mylist)
print('jamal' not in mylist)

mytuple = ('ekfkf' , 75 , True)

print(75 not in mytuple)
print('jamal' not in mytuple)