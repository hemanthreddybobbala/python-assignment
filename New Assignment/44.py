lst = [1, 2, 2, 3, 1, 4]
unique = []
[unique.append(x) for x in lst if x not in unique]
print(unique)

