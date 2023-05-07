list = eval(input("Enter the list:"))
new_list = []
i = 0
while i < len(list):
    new_list = new_list + [list[i]**2]
    i = i+1
print(new_list)
