names = ['ahmed' , 'jomaa' , 'samir', 'batool']
names_formatted = []
for name in names :
    names_formatted.append(name.strip().capitalize())

print(names_formatted)
# عملية تحسين جميع الأسماء داخل قائمة و تحزينها في قائمة أخرى
#-------------------------------
print('-'*50)

def format_string(string : str):
    return string.strip().capitalize()

names_map = map(format_string , names)
# نفس العملية الأولى و لكن من دون الحاجة للحلقة التكرارية التي تستغرق وقتا 
# الأمر يقوم بأخذ قيمة أمر و يقوم بتنفيذه على جميع عناصر قائمة و يخزن الأسماء في كائن ماب
# يمكن تحويل العملية كاملة إلى قائمة و طباعة القائمة
# يمكن أيضاً القيام بعملية فور لوب على العملية لطباعة العناصر فيها

for i in names_map:
    print(i)
    
    