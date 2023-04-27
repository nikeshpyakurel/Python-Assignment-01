# Write a python program to display all the prime numbers within a given range.
inputNumber = int(input("Enter Prime"))

initialValue = 2

print(2)
for i in range(initialValue, inputNumber):
    if i % initialValue != 0:
        print(i)
