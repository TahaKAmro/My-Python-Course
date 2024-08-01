def say_hello(n1 , n2 ,n3 ,n4):
    
    users = [n1 , n2 , n3 , n4]
    
    for user in users :
        
        print(f'Hello {user}')

say_hello('Osama','Ahmed','Samera','Jomana')

#-------------------- 
print('-' * 50)

def say_hello(*users):
    for user in users :
        print(f'hello {user}')
        
names = ('Osama','Ahmed','Samera','Jomana', 'dfvdfs' , 'awrvA', 'sgvdxfvcds')
        
say_hello(*names)