# Write a python program to display all the prime numbers within a given range.
inputRange = int(input('Enter range:'))
for num in range(2, inputRange + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
