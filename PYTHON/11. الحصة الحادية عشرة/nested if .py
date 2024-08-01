name = input('please enter your name : ').capitalize().strip()
gender = input('please enter your gender (male , female) : ').strip()
country = input('please enter your country : ').capitalize().strip()

product = 'My PC'
price = 2000
discount = 0

# تمت في هذا الملف إضافة شرط التعامل مع الجنس
# و ذلك من خلال وضع الجمل الشرطية في جمل شرطية كبيرة
# مما يؤدي إلى قدرة الكود على التعامل مع المعطيات الجديد

if gender == 'male' :
    if country == 'Palestine':
        discount = int((50/100) * price)
        print(f'hello mr {name}, you are from {country}, the final price is {price - discount}')

    elif country == 'Egypt' or country == 'Yemen' or country == 'Lebanon' :
        discount = int((30/100) * price)
        print(f'hello mr {name}, you are from {country}, the final price is {price - discount}')
            
    else :
        discount = int((10/100) * price)
        print(f'hello mr {name}, you are from {country}, the final price is {price - discount}')

else :
    if country == 'Palestine':
        discount = int((50/100) * price)
        print(f'hello mrs {name}, you are from {country}, the final price is {price - discount}')

    elif country == 'Egypt' or country == 'Yemen' or country == 'Lebanon' :
        discount = int((30/100) * price)
        print(f'hello mrs {name}, you are from {country}, the final price is {price - discount}')
            
    else :
        discount = int((10/100) * price)
        print(f'hello mrs {name}, you are from {country}, the final price is {price - discount}')