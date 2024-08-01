def greetings():
    print('oirejdgoser')
    print('fgjkxdfv')
    print('wegffwrhjyn')
    print('sEGFw')
# تعريف أمر يقوم بأربعة أوامر طباعة
# يعتبر هذا الأمر من أنواع الأوامر التي لا تعيد قيمة
greetings() # استدعاء الأمر حتى يتم تنفيذه

#-----------------------
print('-'*50)

def returnavlaue():
    return 12
# تعريف أمر يقوم بإعادة القيمة 12 فقط

returnavlaue() # تنفيذ الأمر لوحده لا يعطي أي نتيجة
print(returnavlaue()) # يجب طباعة الأمر حتى نتمكن من رؤية النتيجة
print(returnavlaue() + 32) # يمكن تنفيذ الحسابات على الأمر لأنه يعيد قيمة رقمية

x = returnavlaue() # يمكن وضع الأمر الذي يعيد قيمة كقيمة لمتغير

print(x)

#-------------------------
print('-'* 50)

def addition(num1 , num2):
    x = num1 + num2
    return x
# تعريف أمر يقوم بأخذ قيمتين و إرجاع قيمة تمثل مجموع القيمتين معاً

print(addition(134 , 123))# الطريقة الأولى لإعطاء القيم التي سيتم تنفيذ الأمر عليها
print(addition(num2= 134 , num1 = 123))# الطريقة الثانية لإعطاء القيم التي سيتم تنفيذ الأمر عليها

def formatter(num1 , num2):
    x = f'first number is : {num1} , second number is : {num2}'
    return x
# تعريف أمر يقوم بأخذ قيمتين و إرجاع جملة مفيدة

print(formatter(134 , 123))# الطريقة الأولى لإعطاء القيم التي سيتم تنفيذ الأمر عليها
print(formatter(num2= 134 , num1 = 123))# الطريقة الثانية لإعطاء القيم التي سيتم تنفيذ الأمر عليها