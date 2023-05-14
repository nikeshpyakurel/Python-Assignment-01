tuple_a = (1, 2, 3)

list_a = list(tuple_a)
list_a.append(4)
tuple_a = tuple(list_a)

print(tuple_a)
