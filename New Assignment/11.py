def function_format(first,last):
    if not last:
        return first
    else:
        return last, first 
first = "hemanth"
last = 'reddy'
print(function_format(first,last))