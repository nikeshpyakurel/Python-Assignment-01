a = int(input('Enter the number'))
c = 2
flag = False
if (a == 1):
    print(f'{a} is not a prime number')
elif (a == 2):
    print(f'{a} is prime no')
else:
    while (c < a):
        if (a % c == 0):
            flag = True
            break
        else:
            flag = False
        c = c+1

    c = c+1
    if (flag):
        print(f"{a} is not a prime")
    else:
        print(f'{a} is prime no')
