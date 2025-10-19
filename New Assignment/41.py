a = [1, 0, 3, None]
b = ['x', '', 'y', 'z']
merged = [(x, y) for x, y in zip(a, b) if x and y]
print(merged)
