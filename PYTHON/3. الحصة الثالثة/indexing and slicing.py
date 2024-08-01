# syntax صيغة الترقيم 
# var_name[index number]

x = 'we love python'
print(x[5]) # use the square brackets to access to any number in the string [int]
#عد المواقع تبدأ من العدد 0 حيث الموقع صفر هنا هو الحرف الأول

x = 'we love python'
print(x[-1]) # accessing the last letter 'n'
#يمكننا الوصول لاخر عناصر من خلال القيمة السالبة

x = 'we love python'
print(x[0:5]) # x[start index : end index]
#عملية التشريح هي عملية أخذ شريحة من النص الكبير من خلال تعيين موضع بداية و موضع نهاية محددين

x = 'we love python'
print(x[:5]) # start from the index 0 untill the end
print(x[2:]) # start from index 2 untill the end
#يمكننا ترك البداية و النهاية فارغتين 

x = 'we love python'
print(x[::1]) # x[the first index : the last index : steps]
print(x[::2]) # x[the first index : the last index : steps]
#نظام الخطوات يقوم بالقفز عن العناصر عبى حسب عدد الخطوات

print(x[::-1])