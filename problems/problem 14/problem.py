n = int(input())
colomns = list(map(int , input().split()))

colomns.sort()
for i in colomns:
    print(i , end = " ")
    
