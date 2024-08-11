n,b,d = map(int,input().split())
sizes = list(map(int,input().split()))
waste = 0
clean = 0
for a in sizes:
    if a <= b:
        waste+=a
        if waste >= d:
            clean+=1
            waste = 0
print(clean)     