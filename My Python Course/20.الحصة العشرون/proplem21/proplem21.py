string = input().strip()
sub_string = input().strip()
cnt=0
start = 0
for i in string:
    x = string.find(sub_string,start)
    if x == -1 :
        break
    else:
        cnt+=1
        start = x+1
        
print(cnt)