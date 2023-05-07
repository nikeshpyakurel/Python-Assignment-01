list = eval(input("Enter the list:"))
i = 0
mul = 1
while i < len(list):
    mul = mul * list[i]
    i = i+1
print(mul)
