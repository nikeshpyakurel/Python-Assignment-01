lst = [1, 2, 3, 4]
list = []
i = 0
while i < len(lst):
    if lst[i] != 2 and lst[i] != 3:
        list.append(lst[i])
    i = i+1
print(list)
