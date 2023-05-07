num = int(input("Enter the number:"))
if num <= 8 and num >= 1:
    i = 1
    while i < 11:
        print(num, "*", i, "=", num*i)
        i = i+1
else:
    print("invalid number")
