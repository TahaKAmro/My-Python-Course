# المهمة الثانية من الواجب السادس بطريقة أخرى

password = input('please enter your password :')
confirm_password = input('please confirm your password :')

while confirm_password != password:
    confirm_password = input('please confirm your password :')

print('access granted')