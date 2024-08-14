n = int(input())
levels = list(range(1,n+1))

x_levels = list(map(int,input().split()))
y_levels = list(map(int,input().split()))
x_levels.remove(x_levels[0])
y_levels.remove(y_levels[0])

total = list(set(x_levels) | set(y_levels))
if total == levels :
    print('I become the guy.')
else :
    print('Oh, my keyboard!')
    