flatten = lambda pairs: [item for pair in pairs for item in pair]
pairs = [(1, 2), (3, 4), (5, 6)]
print(flatten(pairs))