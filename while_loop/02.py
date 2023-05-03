a = eval(input("enter the list of numbers"))
b = 0
sum = 0
while b < len(a):
    sum = sum+a[b]
    b = b+1
print(f"the sum is {sum}")
