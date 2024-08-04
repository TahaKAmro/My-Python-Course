n = int(input())

family = []

for i in range(1,n + 1):
    if n % i == 0:
        family.append(str(i - 1))
        
print(' '.join(family))