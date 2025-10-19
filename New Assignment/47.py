d = {'a': [1, 2], 'b': [3]}
pairs = [(k, v) for k, values in d.items() for v in values]
print(pairs)

