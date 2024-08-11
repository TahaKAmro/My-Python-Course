n = int(input())

counter = 0

for i in range(n):
    status = list(map(int, input().split()))
    if status.count(1) > 1:
        counter+=1

print(counter)