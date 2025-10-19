data = [[[1, 2], [3]], [[4]]]
flat = [x for sub1 in data for sub2 in sub1 for x in sub2]
print(flat)

