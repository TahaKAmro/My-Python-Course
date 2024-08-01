mylist = [12 , 3.3 , 'sdsd' , False , 'SGDF'] # طريقة تعريف القوائم

print(mylist[1])

print(mylist[0:4]) # القوائم تقبل عمليتي الترقيم و التشريح
print(mylist[:4]) # القوائم تقبل عمليتي الترقيم و التشريح
print(mylist[1:]) # القوائم تقبل عمليتي الترقيم و التشريح
print(mylist[::2]) # القوائم تقبل عمليتي الترقيم و التشريح
print(mylist[::-1]) # القوائم تقبل عمليتي الترقيم و التشريح

mylist[0] = 'egfdg' # يمكن استخدام الترقيم لتعيين قيمة عنصر في القائمة

print(mylist)

#--------------------

mylist2 = ['one' , 'two' , 'three'] # يمكننا الدخول إلى العناصر داخل العناصر القوائم

print(mylist2[-1][1]) # اسم القائمة[0][0] هي الطريقة التي ندخل من خلالها الى العنصر الاول في العنصر الاول من القائمة

#-----2d_lists-----

mylist2 = [
    [1,2,3], #0
    [4,5,6], #1 ---> 5 : 1
    [7,8,9], #2
] # عندما نضع قائمة داخل قائمة نسميها بالقائمة ثنائية الأبعاد

print(mylist2[2][2])

#--------------------

mynewlist = [1,2,200,'aesgsdf']

mynewlist.append('easfoh')

print(mynewlist)
# التقنية تقوم بإضافة عنصر جديد -بغض النظر عن نوع البيانات- إلى الموقع الأخير في القائمة
#------------------

a = ['one','two','three']
b = [1,2,3]
a.extend(b)

print(a)
# تقوم التقنية بتوسيع القائمة التي تجرى عليها العملية و تضيف إليها عناصر القائمة الأخرى المعطاة
#------------------

a = [10, 'july' , 0 , -1 , 9.46 , 100 , -223]

a.remove('july')

print(a)
# تقيم التقنية بإزالة عنصر معين
#------------------

b = [10, 23.113 , 0 , -1 , 9.46 , 100 , -223]

b.sort() # للترتيب التنازلي ضع -1 

#[100, 23.113, 10, 9.46, 0, -1, -223]

print(b)
# تقوم التقنية بترتيب القائمة تنازليا او تصاعديا حسب المعطى بين الأقواس
#------------------

c = ['sf',1344 , 23.24 , True]

print(c[::-1])

c.reverse()

print(c)
# تقوم التقنية بعكس القائمة
#------------------

بطيخ = ['sf',1344 , 23.24 , True]

بطيخ.clear()

print(بطيخ)
# تقوم التقنية بتفريغ القائمة من العناصر
#------------------

e = ['one','two','three']

print(e.index('one'))
# تقوم بإحضار رقم موقع العنصر المعطى 
#------------------

f =  ['one','two','three', 1 , True , [12 ,'sa3eed', False ]]
f2 = f.copy()

print(f)
print(f2)

f.clear()
f2.append(243)

print(f)
print(f2)
# تقوم التقنية بنسخ القائمة المعطاة و حفظ نسخة لا تتغير مهما تغيرت الأولى
#------------------

g = [1 ,2 ,3, 2, 5, 22, 54,1,66, 2, 138]

print(g.count(1))
# تقوم التقنية بعد عدد مرات ظهور عنصر معين
#--------------

print(g.pop(3))
# تقوم التقنية بطباعة العنصر المعطى رقمه و إذا لم يعطى اي رقم تطبع اخر عنصر
#-------------------

h =  ['one','two','three', 1 , True ]

h.insert(2 ,False)

print(h)
# تقوم التقنية بإدخال عنصر في موقع معين
#------------------------------------

new_list = ['one','two','three', 1 , True ]

new_list.clear()
new_list.insert(0,'sgsa')

print(new_list)

# من أجل تنفيذ عدة عمليات على قائمة، يجب ان ننفذ كل عملية في سطر على حدة