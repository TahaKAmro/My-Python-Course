x = 5 
if x < 3 :
    print('ok')

# صيغة الجملة الشرطية
# if (condition True or False) :
#   code to do...

#------التمرين الخنفشاري------
name = input('please enter your name : ').capitalize().strip()
# ادخال اسم المستخدم مع تكبير الرف الاول و إزالة المسافات من الجوانب
gender = input('please enter your gender (male , female) : ').strip()
# ادخال جنس المستخدم مع ازالة المسافات من الجوانب
country = input('please enter your country : ').capitalize().strip()
# ادخال البلد مع فعل ما تم فعله بالسم لها

# مواصفات السلعة التي سيتم بيعها
product = 'My PC'
price = 2000
discount = 0

# الشرط الأول ،حيث يتم فحص ما إذا كان الشخص فلسطينياً
if country == 'Palestine' :
    discount = int((50/100) * price) #  حساب المبلغ المخصوم من السعر الكلي و جعله رقما صحيحاً
    print(f'hello mr/mrs {name}, you are from {country}, the final price is {price - discount}')

# الشرط الثاني، إذا كان الشخص عربياً فإنه يحصل على خصم أقل
elif country == 'Egypt' or country == 'Yemen' or country == 'Lebanon' :
    discount = int((30/100) * price)
    print(f'hello mr/mrs {name}, you are from {country}, the final price is {price - discount}')
        
# إذا لم يكن الشخص عربياً فهو أحنبي، و يحصل على خصم أقل
else :
    discount = int((10/100) * price)
    print(f'hello mr/mrs {name}, you are from {country}, the final price is {price - discount}')
    
    
#--------------------------------------------
if country == 'Palestine' :
    discount = (50/100) * price
elif country == 'Egypt' or country == 'Yemen' or country == 'Lebanon' :
    discount = int((30/100) * price)        
else :
    discount = int((10/100) * price)
    
print(f'hello mr/mrs {name}, you are from {country}, the final price is {price - discount}')