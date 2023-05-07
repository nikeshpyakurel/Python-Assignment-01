list = [0, 1, 2, 3, 4, 5, 6]
lst = []
i = 0
while i < len(list):
    if list[i] % 3 != 0:
        lst.append(list[i])
    i = i+1
lst.insert(0, 0)
print(lst)
