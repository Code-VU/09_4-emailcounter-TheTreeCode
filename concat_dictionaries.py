d1 = {1:10, 2:20}
d2 = {3:30, 4:30}
d3 = {5:50, 6:60}
l1 = []
l1.append(d1)
l1.append(d2)
l1.append(d3)
d4 = {}
for d in l1:
    currentdict = d
    for key,value in currentdict.items():
        d4[key] = value
print(d4)