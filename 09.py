# given number is prime or not

inputNumber = int(input("Enter Prime"))

initialValue = 2
if inputNumber == 1:
    print("not prime")

elif inputNumber == 2:
    print("prime")
else:
    for i in range(initialValue, inputNumber, initialValue+1):
        if inputNumber % i == 0:
            print("Not Prime")
            break
        else:
            print("Prime")
            break
