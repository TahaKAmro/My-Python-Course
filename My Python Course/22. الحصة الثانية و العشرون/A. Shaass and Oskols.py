lines = int(input())
birds = list(map(int,input().split()))
shots = int(input())
orders = [list(map(int,input().split()))for _ in range(shots)]
for i in orders:
    wire = i[0]-1
    sht_bird = i[1]
    down_birds= birds[wire]-sht_bird
    upp_birds = sht_bird-1
    birds[wire]=0
    if lines==1:
        birds[wire]=0
        break
    elif wire == 0:
        birds[wire+1]+=down_birds
    elif wire == lines-1:
        birds[wire-1]+=upp_birds
    else:
        birds[wire+1]+=down_birds
        birds[wire-1]+=upp_birds

for i in birds:
    print(i)