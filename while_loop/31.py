given_lst = [111, 32, -9, -45, -17, 9, 85, -10]
lst = []
i = 0
while i < len(given_lst):
    if given_lst[i] > 0:
        lst.append(given_lst[i])
    i = i+1
print(lst)
