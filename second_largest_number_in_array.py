'''
    Second Largest Number In Array
'''

from python_2_3_compatibilty import (input, map, print_function)

def secondLargest(arr):
    _1stHigh = _2ndHigh = float('-inf') # Assign lowest value possible

    for each in arr:
        if each > _1stHigh:
            _2ndHigh = _1stHigh
            _1stHigh = each
        elif each > secondLargest and each < _1stHigh:
            _2ndHigh = each
    
    return _2ndHigh

if __name__ == "__main__":
    arr = list(map(lambda x: int(x), input().split()))
    print secondLargest(arr)


'''
    input:
        12 56 78 98 17 108
    output:
        98
'''
