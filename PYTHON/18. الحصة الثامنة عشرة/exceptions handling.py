try:

    year_of_birth = int(input('enter your birth year: '))
    
    print(2024 - year_of_birth)

except IndexError:
    print('something went wrong')
