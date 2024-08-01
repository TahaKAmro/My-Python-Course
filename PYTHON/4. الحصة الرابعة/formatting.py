
# formatting gives a solution for the concatination problems

# first way (old way)
name = 'Jehad'
age = 15
language = 'Python'
exp = 2.5

print('my name is %s , and im %d years old, i program in language %s , with %.3f years of experience' %(name , age , language,exp))
# في هذه الطريقة يجب علينا تعيين نوع البيانات بالإضافة إلى الاهتمام إلى الترتيب في تعيين المتغيرات بين الأقواس

# ----------الطريقة الثانية --------------
print('-'*50)

name = 'Shehab'
age = 17
language = 'Python'

print('my name is {} , and im {} years old, i program in language {} '.format(name ,age  ,language))
print('my name is {:s} , and im {:d} years old, i program in language {:s} '.format(name ,age  ,language))
print('my name is {:.2s} , and im {:.2f} years old, i program in language {:s} '.format(name ,age  ,language))
print('my name is {1} , and im {0} years old, i program in language {2} '.format(age, name ,language))

# في المرة الأولى نلاحظ اننا لا نحتاج لتعيين نوع البيانات
# في المرة الثانية يمكننا تعيين نوع البيانات
# في المرة الثالثة يمكننا طباعة عدد معين من الحروف في النص او طباعة عدد معين من المنازل العشرية بعد الفاصلة
# في المرة الثالثة يمكننا تعيين أي متغير نريد طباعته في أي موقع من خلال الموقع الرقمي له في الأقواس

money = 22193290482135346432
print('my bank cash is : {:,} '.format(money))
# (,) يمكننا أيضا ترتيب الأعداد الكبيرة باستخدام العلامة 

# ------الطريقة الثالثة------
print('-'*50)

x = 2.1323
age = 16
language = 'Java'

print(f'my name is {x} , and im {age} years old, i program in language {language} ')

# في هذه الطريقة نقوم بإخبار الكود بأننا نريد القيام بعملية تنسيق للنص من خلال وضع حرف الإف كما هو واضح
# ثم نقوم بوضع اسم المتغير بين الأقواس المعقوفة في كل مكان نريد ان نضيف فيه متغيراً

# ----------تطبيق بسيط---------
 
name = 'Taha'
languages = ['python' , 'css' , 'html']
exp = 3.3
age = 16
print(f'Hi , my name is {name} , im {age} years old')
print(f'I can program good websites using {languages[1]} , {languages[0]} , {languages[2]}')
print(f'I have {exp} years of experience .')



















name = 'Odai'
age = 16
programming = ['python', 'html' , 'css']

print(f'hi, your name is {name} , your age is {age} , you program in languages : {programming}')