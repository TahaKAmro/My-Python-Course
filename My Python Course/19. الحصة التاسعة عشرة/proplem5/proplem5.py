z = int(input())
count= 0 
for i in range(1,z):
    if i % 2 == 0 :
        count += 1
print(count)
if count % 2 == 0 :
    print("lose")
else :
    print("win")