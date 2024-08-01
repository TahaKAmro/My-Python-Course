x = 'we love python'
print(len(x))
#هذه التقنية عامة و ليست فقط للنصوص و إنما يمكن استخدامها للقوائم أيضاً

print("-------------------------------------")

# syntax صيغة التقنيات

# var_name.methodname()

x = '   we love python   ' # replace the spaces with anything and try to strip it
print(x.strip()) # try to put another string value in the brackets
#يمكن إعطاء الأمر قيمة أخرى حتى يتم فصل الكلمات بناء عليها

print("-------------------------------------")

x = 'we love python'
print(x.title())
#بناء على قواعد اللغة الانجليزية، كل عنوان تكون كل كلماته تبدأ بحروف كبيرة

print("-------------------------------------")

x = 'we Love Python'
print(x.capitalize())
#تعمل تقنية capitalize على جعل أول حرف في النص capital و جعل باقي الكلمات تبدأ بأحرف small 

print("-------------------------------------")

x , c , z , v = "1","11","111","1111"
print(x.zfill(4))
print(c.zfill(4))
print(z.zfill(4))
print(v.zfill(4))
#تعمل على جعل جميع الأرقام بنفس عدد المنازل من خلال إضافة الصفر خلف الأرقام

print("-------------------------------------")

x = 'We love Python' # change the string to capital
print(x.upper())
print(x.lower())
#التقنيتان متضادتان يمكن من خلالهما رفع الحروف الي صيغة الكابيتال و خفضها إلى صيغة السمول

print("-------------------------------------")

x = 'we love python and programming'
print(x.split()) # takes a second value of maxsplit times
x = 'we-love-python-and-programming' # changing the chareacter between each word
print(x.split('-')) # change the value to any string you want
#عملية تحويل النصوص إلى قوائم من خلال الفصل بينها باستخدام فواصل محددة

print("-------------------------------------")

x = 'Jomana'
print(x.center(10 ,'-')) # 10 is the length of the new string
print(x.center(11 ,'-')) # 11 is the length of the new string
#عملية توسيط النص بين نص اخر محدد عن طريق اعطاء قيمة طول النص الجديد بعض إضافة النصوص الأخرى عليه

print("-------------------------------------")

x = 'k;dajkls fdjvnd kfjvd ifnireljfvldfji n biuf hwopid svmk sfjbd kuhbs lkldf'
print(x.count(' '))
print(x.count('a', 2 , 27 )) # takes also a starting and finishing positions : count('char', start , end)
#يمكننا عد عدد مرات ظهور حرف معين في نص طويل

print("-------------------------------------")

x = 'We loVe python'
print(x.swapcase())
#الأحرف السمول تصير كابيتال و العكس

print("-------------------------------------")

myname = "jehad abo sondos"
print(myname.endswith("s"))
print(myname.startswith("w"))
print(myname.startswith('d', 4 , 10)) # both functions takes a starting and ending positions
#سؤال يتم طرحه على النص حيث يحسب إذا ما كان ينتهي أو يبدأ بنص معين

print("-------------------------------------")

x = 'we love python'
print(x.index('p')) # takes a starting and ending positions
print(x.find('p')) # takes a starting and ending positions
print(x.find('a'))# returns -1 because there's no 'a' in the string
#لا يوجد فرق بين الخاصيتين إلا في التعامل مع القيم الغير موجودة

print("-------------------------------------")

x = 'we love python'
s = 'www.blabla.com'
print(x.replace('o','s')) # replace(old value,new value)
print(s.replace('w','f', 1)) # replace(old value,new value , count) takes how many times we want to replace
#عملية تبديل حرف معين في النص بحرف اخر 

print("-------------------------------------")

x = ['first','second','third']
print(' '.join(x)) # 'string'.join(list)
#عكس عملية الفصل في الأعلى تقوم هذه بدمج النصوص فقط في قائمة عن طريق نص معين

print("-------------------------------------")

x = 'we love python'
print(x.istitle())
#هل النص ينفع أن يكون عنواناً؟؟؟

print("-------------------------------------")

x = ' '
print(x.isspace())
#هل النص يعتبر مسافة فقط ؟؟؟

print("-------------------------------------")

x = 'we love python'
print(x.islower())
#هل النص يتكون من أحرف صغيرة فقط ؟؟؟

print("-------------------------------------")

x = 'we love python'
print(x.isupper())
#هل النص يتكون من أحرف كبيرة فقط ؟؟؟

print("-------------------------------------")

x = 'we'
print(x.isidentifier())
#هل يصلح النص أن يكون اسم متغير ؟؟؟

print("-------------------------------------")

x = 'welovepython'
print(x.isalpha())
#هل يتكون النص من أحرف ابجدية فقط ؟؟؟

print("-------------------------------------")

x = 'we love python'
print(x.isalnum())
#هل يتكون النص من أحرف أبجدية و أرقام ؟؟؟



x = 'zsgc ghndfx'
print(x.upper())
print(x.title())