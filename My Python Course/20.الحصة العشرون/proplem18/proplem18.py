n, k = map(int,input().split())
clouds = list(map(int,input().split()))
power = 100
pos = 0
while True:
    pos+=k
    if pos>=len(clouds):
        pos = pos-len(clouds)
    if clouds[pos]==0:
        power-=1
    else:
        power-=3
    if pos==0:
        break
print(power)