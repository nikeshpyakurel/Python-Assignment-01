a = eval(input("Enter List"))
b = 0
c = len(a)-1
rev = []
while b < len(a):
    rev.append(a[c])
    c = c-1
    b = b+1
print(rev)
