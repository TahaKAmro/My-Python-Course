x = input()
ucount = 0
scount = 0

for i in x :
    if i.isupper():
        ucount+=1
    elif i.islower():
        scount+=1
    
if ucount>scount:
    print(x.upper())
else:
    print(x.lower())