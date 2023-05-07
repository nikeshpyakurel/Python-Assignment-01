string = eval(input("Enter the string:"))
digits = 0
letters = 0
white_space = 0
i = 0
while i < len(string):
    if string[i].isdigit():
        digits = digits + 1
    elif string[i].isalpha():
        letters = letters + 1
    elif string[i].isspace():
        white_space = white_space + 1
    i = i + 1
print(digits)
print(letters)
print(white_space)
