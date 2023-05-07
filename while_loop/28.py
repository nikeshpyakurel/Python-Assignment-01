a = ["ram", "shyam", 1, 2]
i = 0
while i < len(a):
    if type(a[i]) == str:
        print(f"hello!{a[i]}", end=" ")
    i = i+1
