# def curried_version_conversion(m):
#     def inner(n):
#         return n*m
#     return inner
# print(curried_version_conversion(8)(9))
# times8 = curried_version_conversion(7)
# print(times8(2))


#using lambda
sol = lambda m:lambda n: m*n
print(sol(8)(5))