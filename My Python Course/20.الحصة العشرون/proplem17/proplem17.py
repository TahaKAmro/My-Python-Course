candels,need_for_new =  map(int, input().split())
remains = candels
hours = candels

def hours_of_light(hours, remains):
    hours += int(remains/need_for_new)
    remaines_untoched = (remains%need_for_new) + (int(remains/need_for_new))
    
    if remaines_untoched < need_for_new :
        print(hours)
    
    else :
        hours_of_light(hours , remaines_untoched)
    
    

hours_of_light(hours ,remains)