'''
    Solution for sum of arr using recursion
'''

# To import everything use '*'
from python_2_3_compatibilty import (int, map, input)

'''
    @input an array[]
    @returns number
'''
def addTwoNumbers(arr):
    # Base condition
    if (len(arr) == 1): return arr[0]
    return arr[0] + addTwoNumbers(arr[1:])


if __name__ == "__main__":
    arr = map(lambda x: int(x), input('please enter elements seperated by spaces:\n\t').split())
    print(addTwoNumbers(list(arr)))
