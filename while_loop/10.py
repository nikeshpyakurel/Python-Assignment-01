end_range = int(input("Enter the end range: "))

num = 2
while num <= end_range:
    if num > 1:
        is_prime = True
        divisor = 2
        while divisor <= int(num ** 0.5):
            if num % divisor == 0:
                is_prime = False
                break
            divisor += 1
        if is_prime:
            print(num)
    num += 1
