import math
def total(values):
    return sum(values)
def average(values):
    if len(values) != 0:
        sum(values)/len(values)
        return sum(values)/len(values)
    else:
        return math.nan
def median(values):
    values = sorted(values)
    if len(values) == 0:
        raise ValueError
    elif len(values) % 2 ==0:
        return(values[len(values) // 2] + values[len(values) // 2 - 1]) / 2
        
    else:
        return values[len(values) // 2]
