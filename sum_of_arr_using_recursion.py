'''
    Solution for sum of arr using recursion
'''

arr = [1,2,3,4,5]

def addTwoNumbers(arr):
    if (len(arr) == 1): return arr[0]
    return arr[0] + addTwoNumbers(arr[1:])


if __name__ == "__main__": 
    print(addTwoNumbers(arr))
