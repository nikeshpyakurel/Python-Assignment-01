string = eval(input("Enter the string:"))
space = 0
i = 0
while i < len(string):
    if string[i].isspace():
        space = space + 1
    i = i + 1
print(space)
