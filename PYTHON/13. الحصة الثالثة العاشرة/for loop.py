my_list = [1 ,234.34 , 'aefgg',True , 'dgsef']

for item in my_list :
    print(item)
    
print('-'*50)
    
my_string = 'awopitugskljdfn'

for g in my_string:
    print(g)
    
print('-'*50)
    
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers :
    if number % 2 == 0:
        print(f"the number {number} is even")
    else :
        print(f"the number {number} is odd")

        
#------------------------------
print('-'*50)
        
friends_num = int(input('please enter how many friends do you have : '))

friends = []

for i in range(friends_num):
    
    name = input(f'please enter your {i+1} friend : ')
    
    friends.append(name.strip().capitalize())

    
for item in friends :
    
    print(f'#{friends.index(item)+1} {item}')