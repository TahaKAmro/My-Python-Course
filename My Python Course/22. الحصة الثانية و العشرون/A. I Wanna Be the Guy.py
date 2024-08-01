c = int(input())
clist = list(map(int , range(1,c+1)))
x = list(map(int,input().split()))
y = list(map(int,input().split()))
x.remove(x[0])
y.remove(y[0])
able_to_win = []
for i in x :
    able_to_win.append(i)
for i in y :
    able_to_win.append(i)
able_to_win = list(set(able_to_win))

if able_to_win == clist :
    print('I become the guy.')
else :
    print('Oh, my keyboard!')