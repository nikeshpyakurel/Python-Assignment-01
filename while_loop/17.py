num = int(input("Enter the number:"))
i = 1
square = ""
while i < num:
    if i**2 == num:
        square = square + "perfect square"
        break
    i = i+1
if (square):
    print("a perfect square")
else:
    print("not a perfect square")
