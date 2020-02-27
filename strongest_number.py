'''
    Q: Python program to find all Strong Numbers in given list
    A: A Strong Number is a number that is equal to the sum of factorial of its digits.
'''

from python_2_3_compatibilty import (input, map, print_function, division)


'''
    @input number
    @returns factorial of that number
'''
def factorial(num):
    # Base Condition
    if (num < 2): return 1
    else: return num * factorial(num -1)


'''
    @input array
    @output array of strong numbers
'''
def strongest_number(arr):
    strong_number_li = []
    for num in arr:
        sum = 0 # initialising sum
        temp = num
        while (temp):
            remainder = temp % 10 # get the last element
            sum += factorial(remainder) # add factorial to the sum
            temp = temp // 10
        if sum == num: strong_number_li.append(num)
    return strong_number_li

if __name__ == "__main__":
    arr = list(map(lambda x: int(x), input().split()))
    print(arr)
    print(strongest_number(arr))


'''
input : [1, 2, 4 , 5]
ouput : [1, 2]

'''