string = input()
sub_string = input()

pos = 0
cnt = 0

while True:
    x = string.find(sub_string , pos)
    if x == -1:
        break
    else:
        pos = x+1
        cnt += 1
        
print(cnt)
        