numbers = [1, 2, 3,9, 6, 7, 8, 9, 10]

even_count = 0
odd_count = 0

for number in numbers:
  if number % 2 == 0:
    even_count += 1
  else:
    odd_count += 1

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
