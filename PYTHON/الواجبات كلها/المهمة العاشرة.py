# المهمة الأولى من الواجب السادس

number = int(input('please enter a number : '))

fruits = []

for i in range(number):
    
    name = input('enter a fruit : ')
    
    fruits.append(name.strip().capitalize())
    
for fruit in fruits:
    
    if len(fruit) <= 7:
        
        print(fruit)