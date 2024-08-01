# الحلقة اللانهائية-------------------------

#a = 5
#while a > 3 :
#    print(a)

#---------------------------------------

a = 'se;oidjcgfb.'
counter = 0
while counter < 5 :
    print(a)
    counter+=1

# العداد = 0
# طالما العداد > عدد مرات إعادة الكود
# زيادة العداد بمقدار 1
#    print(a)
# الناتج طباعة القيمة بعدد مرات تكرار الحلقة

#--------التمرين----------
print('-'*50)

friends_num = int(input('please enter how many friends do you have : '))
# يطلب من المستخدم ادخال عدد اصدقائه

friends = []
# إنشاء قائمة فارغة لوضع الأصدقاء الذين سيتم إدخالهم

counter = 0
# استعمال عداد من أجل تحديد عدد مرات تكرار الحلقة التكرارية

while counter < friends_num : # طالما العداد لم يبلغ عدد الأصدقاء الذين تم إدخالهم
    
    name = input(f'please enter your {counter+1} friend : ')
    # عملية إدخال اسم صديق صاحب رقم معين
    
    friends.append(name.strip().capitalize())
    # يتم إدخال اسم الصديق مع إجراء بعض التغييرات عليه
    
    counter += 1
    # زيادة العداد
    
print(friends)
# طباعة قائمة الأصدقاء للتأكد من سير الكود

counter2 = 0
# بدء عداد جديد استعداداً لتنفيذ الحلقة التكرارية الثانية

while counter2 < friends_num: # طالما أن العداد أصغر من عدد الأصدقاء المدخل
    
    print(f'#{counter2+1} {friends[counter2]}') # طباغة اسم الصديق من القائمة مع رقمه
    
    counter2 += 1
    # زيادة العداد
    
print('loop is over')