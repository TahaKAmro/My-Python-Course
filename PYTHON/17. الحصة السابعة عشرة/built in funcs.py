print(all([False , True , True]))
print(all([True , True , True]))
print(all([0 , 1 , 1]))
# يقوم الأمر بفحص ما إذا كانت كل عناصر القائمة تحمل القيمة المنطقية (True)
#----------------------------
print('-'*50)

print(any([False , True , True]))
print(any([True , True , True]))
print(any([0 , 1 , 1]))
# يقوم الأمر بفحص ما إذا كان أحد عناصر القائمة يحمل القيمة (صحيح) على الأقل
#----------------------------
print('-'*50)

print(bin(3000))
# يقوم الأمر بإرجاع القيمة الثنائية لأي عدد
#----------------------------
print('-'*50)

x = 'zdfhfcgb'

print(id(x))
# يقوم الأمر بإعادة  الموقع التخزيني للمتغير في الذاكرة العشوائية
#----------------------------
print('-'*50)

mylist = list(range(1,6))

print(sum(mylist))
# يقوم الأمر بإعادة مجموع الأعداد في قائمة
#----------------------------
print('-'*50)

print(round(1232.13 , 1))
print(round(1232.56 , 1))
print(round(1232.563 , 3))
# يقوم الأمر بتقريب الأعداد العشرية بحسب عدد معين من المنازل بعد الفاصلة
#--------------------
print('-'*50)

print(range(1,10))
print(list(range(1,10)))
print(list(range(0,10,3)))

#---------------------------------
print('-'*50)

print('hello', 'oefjvisdho','qwrgaf', sep='------')
# الخاصية الأولى لأمر الطباعة و التي تختص بالفاصل بين النصوص التي تتم طباعتها

mylist = ['ahmed' , 'yosra', 'jameel']

for i in mylist:
    print(i , end='///////') 
# الخاصة الثانية بأمر الطباعة و التي تقوم بإنهاء أمر الطباعة بطريقة مميزة و تكون بالأساس قيمتها البدء بسطر جديد
    
print('szdhbfxdg') # لاحظ طباعة الأمر في نفس سطر الحلقة التكرارية

#------------------------------
print('-'*50)

print(abs(-113))
# أمر القيمة المطلقة
#----------------------------
print('-'*50)

print(pow(4,2)) # 4**2
print(pow(4,2,3)) # (4**2) % 3
#----------------------------
print('-'*50)

mylist = [4323,352,634,534,6453,65]

print(min(mylist)) # أعلى رقم في القائمة
print(max(mylist)) # أصغر رقم في القائمة

#----------------------------
print('-'*50)

mylist = ['one','Two','Three','Four','Five','Six']
mylistnumbered = enumerate(mylist) # enumerate(iterable , start=0)

for number,element in mylistnumbered :
    print(f'{number} -> {element}')

#-------------------------------
print('-'*50)

x = [1,2,3,4,5,6,7,8,9]

print(x[::-1])
print(list(reversed(x)))