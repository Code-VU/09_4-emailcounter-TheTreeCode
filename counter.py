def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
    people = dict()
    for line in handle:
        if line.startswith('From '):
            line = line.split()
            person = line[1]
            people[person] = people.get(person, 0) + 1
    findgreatestvalueindictionary(people)

def findgreatestvalueindictionary(dictionary):
    currentvalue = 0
    currentkey = None
    for key,value in dictionary.items():
        if value > currentvalue:
            currentvalue = value
            currentkey = key
    print(currentkey,currentvalue)

        

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()


'''
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of
mail messages. The program looks for 'From ' lines and takes the second word of those lines as the
person who sent the mail.

The program creates a Python dictionary that maps the sender's mail address to a count of the number
of times they appear in the file. After the dictionary is produced, the program reads through the
dictionary using a maximum loop to find the most prolific committer.

Starter Code
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
Desired Output
cwen@iupui.edu 5
'''