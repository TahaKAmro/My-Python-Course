n = int(input())
wanted_house = int(input())

right_side = []
left_side = []

for num in range(1 , n*2+1):
    if num % 2 == 0:
        right_side.append(num)
    else:
        left_side.append(num)
        
left_side.sort(reverse=1)

if wanted_house % 2 == 0:
    position = right_side.index(wanted_house)
    print(left_side[position])
else:
    position = left_side.index(wanted_house)
    print(right_side[position])