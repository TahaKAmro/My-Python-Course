num = int(input())

evens = 0

for i in range(1,num):
    if i % 2 == 0:
        evens += 1
    
print(evens)
if evens % 2 == 0:
    print('lose')
else :
    print('win')