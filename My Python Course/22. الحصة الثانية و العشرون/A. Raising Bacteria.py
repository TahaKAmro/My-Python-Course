i_want = int(input())

days = [1]
bacterias_added = 1
while True:
    days.append(days[-1]*2)
    if days[-1] == i_want or i_want == 1:
        break
    if i_want > days[-2] and i_want < days[-1]:
        i_want-=days[-2]
        days = [1]
        bacterias_added +=1
        
print(bacterias_added)