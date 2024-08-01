# المتغيرات تحتمل اي نوع بيانات 
# المتغيرات يمكن تغييرها في الكود إلى أي قيمة

#--------------------------
#--قواعد كتابة اسماء المتغيرات--
#--------------------------
# 1-يجب أن يكون أول حرف حرفاً أبجدياً (A....Z):
#---> we can't name a variable as : /name or %name or #name
# 2-لا يمكن أن يكون أول حرف رقماً :
#---> we can't name a variable as : 2name or 324.21name
# 3-يمكن تضمين الأرقام داخل اسم المتغير و ليس في بداية اسمه :
#---> we can name a variable as : name2 or na2me or name1312
# 4-لا يمكن أن يحتوي اسم المتغير على علامات مميزة (@,#,$,%,-,+...):
#---> we can't name a variable as : name* or na-me or (my name) we can't use space
# 5-name is not like Name [case sensitive] :
#---> when a variable named (name) we can't call it as (Name)

#-----------------------------------------------------------
x = 10  #giving a value of 10 and its a number
x = 'HI' #changing the 'x' value to something else
print(x)
# بايثون تمكننا من تعريف متغير وتغيير قيمته مع تغيير نوع البيانات التي قد يحملها
#-----------------------------------------------------------

#---------concatination---------
name = 'sameer' # الاسم هو نص
age = '17' # العمر في الأساس رقم و لكن يتم اعتباره نصاً هنا حتى نتمكن من دمجه مع باقي النصوص في الرسالة

print('hi , my name is '+ name +' and im '+ age +' years old')
# عملية دمج النصوص باستخدام العلامة + حيث لا يمكن دمج النصوص بالأرقام
# جرب تغيير نوع بيانات العمر إلى رقم و اقرا الإيرور الذي سيظهر
#-------------------------------

#-----تعيين متغيرات متعددة في نفس السطر-----
x,y,z = 121 , 'My name is hosam', 13 
print(x)
print(y)
print(z)
# جرب إزالة احد القيم مرة و إزالة إحدى المتغيرات مرة أخرى

help('keywords')


# syntax صيغة المتغيرات
 
# var_name = value

var_name = 'sdojf'
var_name = 121
var_name = [214,25,6,23]