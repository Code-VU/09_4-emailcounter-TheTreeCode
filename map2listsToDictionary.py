l1 = ['a','b','c']
l2 = [1,2,3]
d1 = dict()
counter = 0
for i in l1:
    d1.setdefault(i, l2[counter])
    counter += 1

print(d1)