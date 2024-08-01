a,b,d = map(int , input().split())
oranges = list(map(int , input().split()))
times = 0
tank = 0
for i in oranges:
    if i > b:
        continue
    else :
        tank+=i
        if tank>d:
            tank = 0
            times+=1
print(times)
    