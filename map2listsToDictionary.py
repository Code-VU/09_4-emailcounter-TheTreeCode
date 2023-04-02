letters = ['a','b','c']
numbers = [1,2,3]
d1 = dict(zip(letters,numbers))
filetocreate = open(input('Enter a file name that you would like to add this dictionary to: '), 'w')
filetocreate.write(str(d1))
filetocreate.close()
print(d1)