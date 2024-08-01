#--integer vlaues conversion--
a = 12
b = 15.99
c = '3'

print(int(b)) # تحويل قيمة من عدد عشري إلى عدد صحيح float --> int
print(int(c)) # تحويل قيمة نصية إلى عدد عشري int --> float
print(int(c) + 10) # تحويل قيمة نصية إلى عددية و إجراء عملية حسابية عليها للتأكد
print(float(a)) # تحويل عدد صحيح إلى عدد عشري int --> float

c = int(c) # تجديد قيمة النص و تحويله إلى رقم

print(type(c)) # طباعة نوع المتغير للتأكد من تحوله إلى رقم
print(c + 10) # اداء عملية للتأكد من تحوله

print(str(a) * 50) # تحويل الرقم إلى نص و القيام بعملية تكرار النص للتأكد من نجاح العملية

#-----------------------
print('-'*50)

mystring = 'the weather is good'
mylist = [1,3,True , 'woef']
mytuple = (1,3,True , 'woef')
myset = {1,3, True , 'woef'}
mydict = {
    'one' : 1,
    'two' : 2
}

#-- str --> others ---
print(list(mystring)) # تحويل النص إلى قائمة مما يؤدي إلى وضع كل عنصر أو حرف كعنصر مستقل في القائمة
print(tuple(mystring)) # نفس مبدأ القائمة
print(set(mystring)) # نفس مبدأ القائمة و لكنه يزيل العناصر المكررة
#print(dict(mystring))

#-- list,tuple,set --> others --
print(str(mylist)) 
print(tuple(mylist))
print(set(mylist))
# تحويل القوائم و الأوعية و المجموعات إلى بعضها البعض و إلى نص
#------------------------
print('-'*50)

mylist2 = [['a', 1], ['b' , 2]]
mytuple2 = (('a' , 1), ('b', 2))

print(dict(mylist2))
print(dict(mytuple2))
# الطريقة الوحيد لتحويل القوائم و الأوعية إلى قواميس من خلال الاعتماد على مبدأ ثنائيات الأبعاد
# تمثل القوائم الداخلية التي تحتوي على قيمتين حيث القيمة الأولى هي المفتاح و القيمة الثانية هي الفاليو