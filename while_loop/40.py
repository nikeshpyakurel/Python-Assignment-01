givenList = [1, 2, 3, 4]
i = 0
while i < len(givenList):
    if givenList[i] == 3:
        givenList.remove(3)
        givenList.insert(i-1, 'a')
    i = i+1
print(givenList)
