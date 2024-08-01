# المهمة الثانية من الواجب السادس 

password = input('please enter your password :')
confirm_password = input('please confirm your password :')
while True :
    if password == confirm_password :
        print ('acces sucsesfuly')
        break
    else :
        confirm_password = input('please confirm your password :')