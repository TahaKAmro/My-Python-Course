wanted = 12

added = 0

while wanted > 0:
    if wanted % 2 != 0:
        added += 1
    wanted = int(wanted/2)
    
print(added)