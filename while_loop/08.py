a = [1, 2, 3, 4]

c = 0

while c < len(a):
    if a[c] == 1:
        a.remove(1)
        a.append(5)
    c = c+1
print(a)
