def swap(a, b):
    temp = 0
    temp = a 
    a = b
    b = temp
    return a, b
a, b = 8, 1
print(swap(a, b))