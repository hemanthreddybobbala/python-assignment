def make_multipler(m):
    def input(n):
        return m * n
    return input
multiple = make_multipler(2)
print(multiple(3))


#lambda version
sol = lambda x:lambda y:x*y
times7 = sol(9)
print(times7(8))