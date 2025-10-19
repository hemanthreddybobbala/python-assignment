def apply_if(func, predicate, iterable):
#     result = []
#     for item in iterable:
#         if predicate(item):
#             result.append(func(item))
#     return result
# def double(x):
#     return x * 2
# def is_even(x):
#     return x % 2 == 0

# numbers = [1, 2, 3, 4, 5]
# filtered = apply_if(double, is_even, numbers)
# print(filtered)  
    return [func(x) for x in iterable if predicate(x)]
sol = apply_if(lambda x:x*2,lambda x:x % 2,[1, 2, 3, 4, 5])
print(sol)

