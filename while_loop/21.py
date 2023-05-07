num = int(input("Enter the number:"))
i = 0
odd = 0
while i < num:
    if i % 2 != 0:
        odd = odd + i
    i = i + 1
print(odd)
