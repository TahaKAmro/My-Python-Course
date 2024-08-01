sami = int(input())
jameel = int(input())

years = 0

while jameel >= sami:
    jameel *= 2
    sami *= 3
    years += 1
    
print(years)
