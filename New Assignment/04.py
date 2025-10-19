def string(s):
    b = len(s)
    c = len(set(s))
    return b,c
s = 'HemanthReddy'
b, c = string(s)
print('No of elements in string',b)
print('No of unique elements in string',c)