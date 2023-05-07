bad_chars = [';', ':', '!', "*"]
string = "py;th* o:n ! ;py * t*h:o !n"
i = 0
while i < len(bad_chars):
    string = string.replace(bad_chars[i], "")
    string = string.replace(" ", "")
    i = i+1
print(string)
