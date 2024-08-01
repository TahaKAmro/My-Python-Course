for number in range(1,11):
    if number == 7 :
        continue
    print(number)
# يقوم الكود في الأعلى بالقفز عن العدد سبعة ولا يطبعه باستخدام الفور لوب
#-------------------
print('-'*50)

cnt = 0
while cnt < 10:
    cnt += 1
    if cnt == 7:
        continue
    print(cnt)

# يقوم الكود بنفس عمل الكود الذي يسبقه ولكن باستخدام الوايل لوب
#------------------
print('-'*50)

cnt = 0
while True :
    if cnt == 5 :
        break

    print(cnt)
    cnt+=1
    
# يقوم الكود بإيقاف الحلقة التكرارية عندما يصل العداد إلى 5
#---------------------------------
print('-'*50)

mylist = ['hamzeh' , 'sakhr', 'dana', 'diab']

for i in mylist:
    if i == 'dana':
        break
    print(i)
    
# عندما تصل الحلقة التكرارية إلى العنصر دانا تتوقف الحلقة
#-------------------------------    

# استخدام الأمر pass

cnt = 0
while cnt < 3:
    cnt += 1
    pass

if 3 < 7 :
    pass

for i in range(10):
    pass