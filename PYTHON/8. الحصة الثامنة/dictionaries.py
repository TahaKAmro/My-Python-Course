student = {
    'name':'deyaa',
    'age' : 13 ,
    'class' : 7 ,
    'firends' : ['dsjk', 'aigdf', 'qrji'],
} # هذه هي طريقة تعريف القواميس

print(student['name']) 
print(student.get('name'))
# باستخدام احدى الطريقتين، يمكننا الحصول على القيم الموجودة داخل القاموس

student['name'] = 'Yaseen'
# بما ان القواميس متغيرة، يمكننا تعيين قيمة مفتاح من خارج القاموس

print(student)

#--------------------
print('-' *50)

print(student['firends'][1])
# محاولة الوصول إلى عنصر داخل القائمة الموجودة داخل القاموس

#--------------------
print('-' *50)

students = {
    1 : {
        'name' : 'malik',
        'age' : 13,
    },
    2 : {
        'name' : 'sawsan',
        'age' : 15,
    }
} # (2d dictionary) قاموس ثنائي الأبعاد 

print(students)
print(students[2]['name'])
print(len(students))
# طريقة التعامل مع القواميس ثنائية الأبعاد

#------------------------
print('-' *50)

school = {
    'name' : 'ewopifjbj',
    'students_number' : 600, 
    'classes' : 30,
    'manager' : 'raed',
}

print(school.keys()) # تقوم هذه التقنية بإعادة كل المفاتيح داخل القاموس
print(school.values()) # تقوم هذه التقنية بإعادة كل القيم الموجودة داخل القاموس


#-------------------
print('-' *50)

ahmed= {
    'age' : 16 ,
    'class' : 11
}

print(ahmed)
ahmed.clear()
print(ahmed)
# تقوم هذه التقنية بتفريغ القاموس من محتوياته

#------------------
print('-' *50)

toyota = {
    'model': 2014,
    'owner' : 'elzalameh',
}

toyota2 = toyota.copy()

print(toyota)
print(toyota2)

toyota['model'] = 2015 # تغيير قيمة المفتاح

print(toyota)
print(toyota2)
# تقوم هذه التقنية بنسخ القاموس و لا تتغير النسخة مهما تغير القاموس الأول


toyota.update({'speed' : 150})
# تقوم هذه التقنية بإضافة مفتاح و قيمته إلى القاموس و ذلك من خلال إضافة عنصر قاموس كامل بين الأقواس

toyota['wrfwd'] = 2423 # طريقة أخرى لإضافة مفتاح و قيمة إلى القاموس

print(toyota)