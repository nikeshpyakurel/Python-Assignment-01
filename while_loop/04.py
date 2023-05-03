given_list = [1, 'a', 'c', 2, 3, 4]
b = 0
while b < len(given_list):
    if type(given_list[b]) == int:
        print(given_list[b])
    b = b+1
