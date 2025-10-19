from functools import reduce
mult = lambda *args: reduce(lambda x, y: x * y, args)
print(mult(5,6))