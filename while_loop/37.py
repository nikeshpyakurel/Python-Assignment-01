num = int(input("Enter the number:"))
i = 0
even = 0
odd = 0
while i < num+1:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
    i = i+1
print(even)
print(odd)
