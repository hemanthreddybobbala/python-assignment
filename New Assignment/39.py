students = [{'name':'A','score':80}, {'name':'B','score':60}]
for items in students:
    if items['score'] >= 75:
        print(items.values())