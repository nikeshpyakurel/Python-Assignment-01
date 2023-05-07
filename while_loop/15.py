string = input("Enter the number:")
reverse = ""
i = 0
while i < len(string):
    reverse = string[i] + reverse
    i = i + 1
if reverse == string:
    print("palindrome")
else:
    print("not palindrome")
