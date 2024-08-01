x,z = map(int,input().split())
count = 0
while x<=z:
    x*=3
    z*=2
    count+=1

print(count)