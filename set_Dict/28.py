marks = {
    'Subu': {'Maths': 88, 'Eng': 60, 'SSt': 95},
    'Amol': {'Maths': 78, 'Eng': 68, 'SSt': 89},
    'Raka': {'Maths': 56, 'Eng': 66, 'SSt': 77}
}
english = marks['Subu']['Eng']
print(f"the marks of subu in english is {english}")
marks['Raka']["Maths"] = 77
print(marks['Raka'])
