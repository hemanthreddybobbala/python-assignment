def inner_demo():
    def inner_function():
        return f'calling the inner function'
    print(inner_function())
    return 0
print(inner_demo())