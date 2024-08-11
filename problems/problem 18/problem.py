word = input()
small = 0
cpital = 0
for letter in word:
    if letter.islower():
        small+=1
    else:
        cpital+=1
        
if small>=cpital:
    print(word.lower())
else:
    print(word.upper())