def fact(x):
    if x == 0:
        return 1
    else :
        return x*fact(x-1)
# أمر يقوم بحساب قيمة مضروب العدد من خلال استدعاء نفسه مراراً و تكراراً

print(fact(3))

#-------------------------
print('-'*50)

word = input('please enter any word: ') # يتم إدخال كلمة لتطبيق الأمر عليها

#print(word[0])

#print(word[1:])

def cleanword(word):
    print('-'*50)
    if len(word) == 1:
        return word 
        # الشرط الأول
        # حالة شاذة، إذا كان عدد حروف الكلمة 1 يتم إعادة الكلمة
    print(f'your word is :{word}')
    if word[0] == word[1]:
        print('removing the first letter')
        print(f'repeating the proccess on {word[1:]}')
        return cleanword(word[1:])
        # الشرط الثاني
        # إذا وجد أن الحرف الأول مساوٍ للحرف الثاني يتم تنفيذ الأمر مجدداً على الكلمة نفسها دون الحرف الأول
    else :
        print('second condition is on')
        print('adding the first letter to it')
        return word[0] + cleanword(word[1:])
        # الشرط الأخير
        # إذا لم يكن الحرف الأول مساوياً للحرف الثاني، يتم تخزين الحرف الأول و دمجه بقيمة تنفيذ الكود على ما تبقى من الكلمة

print(cleanword(word)) # استدعاء الأمر و طباعة الناتج