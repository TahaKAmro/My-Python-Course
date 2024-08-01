students = {
    1 : {
        'name' : 'rogkj',
        'age' : 13 , 
        'date' : '22/7/2011'
    },
    2 : {
        'name' : 'sthsj',
        'age' : 14 , 
        'date' : '22/7/2010'
    },
    3 : {
        'name' : 'kohjfj',
        'age' : 15 , 
        'date' : '22/7/2009'
    },
}
print(students[1]['name'],students[2]['name'],students[3]['name'])

print(students[1]['age'],students[2]['age'],students[3]['age'])
print(students[1]['date'],students[2]['date'],students[3]['date'])

claas = 'c' 
students[1].update({'class': claas})
students[2].update({'class': claas})
students[3].update({'class': claas})

print(students)