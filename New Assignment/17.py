def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
n = 4
print('fact of n is',fact(n))
    