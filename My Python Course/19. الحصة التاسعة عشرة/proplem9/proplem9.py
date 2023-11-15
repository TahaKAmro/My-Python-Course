one = ["Q","R","O","P",'A','D']
two = ['B']
string = input()
count = 0

if len(string) <= 40 :
    for i in string.upper() :
        if i in one :
            count+=1
        elif i in two:
            count += 2
    print(count)

    