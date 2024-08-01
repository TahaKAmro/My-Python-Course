my_list = ['   ahmed', 'esraa    ' , '   rama', '   omar   ']

for item in my_list:
    newitem = item.strip().capitalize()

    my_list[my_list.index(item)] = newitem
    
print(my_list)