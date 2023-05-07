ranges = int(input("Enter the range: "))

num = 2
while num <= ranges:
    if num > 1:
        div = 2
        prime = True
        while div <= int(num ** 0.5):
            if num % div == 0:
                prime = False
                break
            div += 1
        if prime:
            print(num)
    num += 1
