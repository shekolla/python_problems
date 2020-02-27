'''
    Find the middle elements in the string
    if length is odd return single element
    else return two elements
'''

from python_2_3_compatibilty import (input, print_function)

'''
    @input string
    @return the middle element
'''

def get_middle_elements(st):
    mid = len(st) // 2
    if (len(st) % 2 == 0):
        return st[mid] + st[mid + 1]
    return st[mid]

if __name__ == "__main__":
    print (get_middle_elements(input()))


'''
input: 123
output: 2

input: abcd
output: bc

''' 