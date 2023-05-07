num = input("Enter the number:")
b = len(num)
armstrong = 0
i = 0
while i < b:
    armstrong = armstrong + int(num[i])**b
    i = i + 1
if armstrong == int(num):
    print("armstrong number")
else:
    print("not armstrong")
