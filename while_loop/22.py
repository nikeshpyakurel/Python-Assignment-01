num = int(input("Enter the number:"))
i = 0
even = 0
while i < num:
    if i % 2 == 0:
        even = even + i
    i = i + 1
print(even)
