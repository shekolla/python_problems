'''
    fibbinoci numbers
'''

# recurrsion
def fibbinoci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibbinoci(n-1) + fibbinoci(n-2)


# dynamic
def fibbinoci_dynamic(n):
    fib = { 0:0, 1:1 } # initilizing
    for i in range(2, n +1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

# testing
for i in range(11): print(fibbinoci_dynamic(i))