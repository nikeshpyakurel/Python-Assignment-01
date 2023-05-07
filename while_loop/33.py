list = eval(input("Enter the list:"))
integer = []
string = []
i = 0
while i < len(list):
    if type(list[i]) == int:
        integer.append(list[i])
    elif type(list[i]) == str:
        string.append(list[i])
    i = i+1
print(integer)
print(string)
