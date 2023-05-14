a = {"salary": 20, "age": 90}
sorted_a = sorted(a.keys())
print("Sorted dictionary by key in ascending order:")
for key in sorted_a:
    print(key, a[key])
sorted_a = sorted(a.values(), reverse=True)
print("Sorted dictionary by value in descending order:")
for value in sorted_a:
    print(value)
