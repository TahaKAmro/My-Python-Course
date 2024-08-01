price = int(input())
days = int(input())
steps = list(map(int,input().split()))

discount = 0

if steps[0]>=200 and steps[1]==steps[0]*2:
    discount+=1
    for i in range(1,days):
        today = steps[i]
        yesterday = steps[i-1]
        if today == yesterday*2:
            discount+=1
        else:
            break
print("Discount =", price*(discount/days))
print("Net Cost =", price-(price*(discount/days)))