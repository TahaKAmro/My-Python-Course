candils , needed_for_new = map(int , input().split())
hours = candils
remains = candils

def hours_of_light(hours , remains):
    new_candils = int(remains/needed_for_new)
    hours += new_candils
    remains_untouched = (remains%needed_for_new) + new_candils
    
    if remains_untouched < needed_for_new:
        print(hours)
    else:
        hours_of_light(hours , remains_untouched)
        
hours_of_light(hours , remains)