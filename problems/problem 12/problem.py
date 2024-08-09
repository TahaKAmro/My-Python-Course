n,k = map(int, input().split())
clouds = list(map(int,input().split()))

power = 100
position = 0

while True:
    position += k
    if position >= n:
        position -= n

    if clouds[position] == 0:
        power -= 1
    else :
        power -= 3
    
    if position == 0:
        break
    
print(power)