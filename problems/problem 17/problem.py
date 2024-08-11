wires_num = int(input())
birds_on_wires = list(map(int, input().split()))
shots_num = int(input())
shots = []
for i in range(shots_num):
    shot = list(map(int,input().split()))
    shots.append(shot)
    
for i in shots:
    shooted_wire = i[0]-1
    shooted_bird = i[1]-1
    on_the_lift = birds_on_wires[shooted_wire] - shooted_bird - 1
    on_the_right = shooted_bird 
    upper = shooted_wire-1
    lower = shooted_wire+1
    if wires_num == 1:
        birds_on_wires[shooted_wire] = 0
        break
    if shooted_wire == 0:
        birds_on_wires[lower] += on_the_lift
        birds_on_wires[shooted_wire] = 0
    elif shooted_wire == wires_num-1:
        birds_on_wires[upper] += on_the_right
        birds_on_wires[shooted_wire] = 0
    else:
        birds_on_wires[shooted_wire] = 0
        birds_on_wires[upper] += on_the_right
        birds_on_wires[lower] += on_the_lift
        
print(birds_on_wires)