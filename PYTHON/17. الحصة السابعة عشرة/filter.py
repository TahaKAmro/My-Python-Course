names = ['sara' , 'jameel' , 'Samir' , 'sameera']

def startwiths(name:str):
    return name.strip().capitalize().startswith('S') 

names_filtered = tuple(filter(startwiths , names))

print(names_filtered)