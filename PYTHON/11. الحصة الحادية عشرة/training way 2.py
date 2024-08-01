#------التمرين الخنفشاري------
# في هذا الملف تم اختصار الكود لأن أمر الطباعة هو أمر مشترك بين جميع الشروط

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

if country == 'Palestine' :
    discount = (50/100) * price
    
elif country == 'Egypt' or country == 'Yemen' or country == 'Lebanon' :
    discount = int((30/100) * price)  
          
else :
    discount = int((10/100) * price)
    
print(f'hello mr/mrs {name}, you are from {country}, the final price is {price - discount}')