letters = input().upper()

one_hole = ['A' , 'D' , 'O' , 'P' , 'R', 'Q']
two_holes = ['B']

holes = 0

if len(letters) < 40:
    for i in letters:
        if i in one_hole:
            holes+=1
        elif i in two_holes:
            holes += 2
            
    print(holes)