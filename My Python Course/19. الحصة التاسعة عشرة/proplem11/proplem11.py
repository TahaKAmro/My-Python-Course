n= int(input())
fam = []
for i in range(1,n+1):
    if n % i == 0:
        fam.append(str(i-1))
print(" ".join(fam))