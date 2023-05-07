given_list = [1, 2, 3, 4]
lst = []
i = 0
while i < len(given_list):
    lst = lst + [given_list[i]**3]
    i = i + 1
print(lst)
