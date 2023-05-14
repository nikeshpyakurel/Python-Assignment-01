# i = 0
# while i <= 50:
#     if i > 7:
#         break
#     else:
#         print(i)
#     i = i+1


# 2. given input a="ram"
# expected output="mAr"
i = 0
a = 'ram'
b = ''

while i < len(a):
    if i == len(a)-3:
        b = a[i].lower()+b
    elif i == len(a)-2:
        b = a[i].upper()+b
    else:
        b = a[i].lower()+b
    i = i+1
print(b)
