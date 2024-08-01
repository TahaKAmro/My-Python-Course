#------التمرين الخنفشاري------
# في هذا الملف تم الاعتماد على الطريقة الثانية في الحل
# و لكن مع تغيير طريقة تعاملنا مع الشرط الثاني من خلال وضع البلدان العربية في قائمة و سؤال هل البلد المدخل ضمن القائمة ؟؟؟

name = input('please enter your name : ').capitalize().strip()
# ادخال اسم المستخدم مع تكبير الرف الاول و إزالة المسافات من الجوانب
gender = input('please enter your gender (male , female) : ').strip()
# ادخال جنس المستخدم مع ازالة المسافات من الجوانب
country = input('please enter your country : ').capitalize().strip()
# ادخال البلد مع فعل ما تم فعله بالسم لها

# تعريف البلدان العربية في قائمة
arab = ['Lebanon','Tunisia','Jordan','Egybt']

# مواصفات السلعة التي سيتم بيعها
product = 'My PC'
price = 2000
discount = 0

if country == 'Palestine' :
    discount = (50/100) * price
    
# اذا كان البلد ضمن القائمة يعيد القيمة صحيحة
elif country in arab :
    discount = int((30/100) * price)  
          
else :
    discount = int((10/100) * price)
    
print(f'hello mr/mrs {name}, you are from {country}, the final price is {price - discount}')