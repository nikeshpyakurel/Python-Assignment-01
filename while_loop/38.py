
lst = [1, 2, 3, 4]
a = []
i = 0
while i < len(lst):
    if lst[i] != 3:
        a.append(lst[i])
    i = i+1
print(a)
