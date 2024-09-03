file_name = "text.txt"
maxlen = 0
count = 0
with open(file_name, "r") as f:
    s = f.read()
    for i in range(len(s)):
        if s[i] == 'X':
            count += 1
            if maxlen < count:
                maxlen = count
        else:
            count = 0


# if maxlen < count:
#     maxlen = count



print(maxlen)


