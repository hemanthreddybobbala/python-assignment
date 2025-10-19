a = ['a b','c d e']
hem = [list1 for str in a  for list1 in str.split()  ]
print(hem)