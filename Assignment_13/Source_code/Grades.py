import math
def total(values):
    '''Returns the total of the list'''
    return sum(values)
def average(values):
    '''Returns the average of the list'''
    if len(values) != 0:
        sum(values)/len(values)
        return sum(values)/len(values)
    else:
        return math.nan
def median(values):
    '''Returns the median of the list'''
    values = sorted(values)
    if len(values) == 0:
        raise ValueError
    elif len(values) % 2 ==0:
        return(values[len(values) // 2] + values[len(values) // 2 - 1]) / 2
        
    else:
        return values[len(values) // 2]
