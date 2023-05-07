num = int(input("Enter the number:"))
perfect_num = 0
i = 1
while i < num:
    if num % i == 0:
        perfect_num = perfect_num + i
    i = i + 1
if perfect_num == num:
    print("It is a perfect number")
else:
    print("It is not a perfect number")
