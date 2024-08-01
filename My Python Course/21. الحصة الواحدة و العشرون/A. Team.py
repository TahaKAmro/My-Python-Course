x = int(input())
count = 0
for i in range(x):
    sullutions = list(map(int , input().split()))
    if sullutions.count(1) > 1:
        count+=1
print(count)