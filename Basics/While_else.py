
data = [1, 2, 3]
value = 10
index = 0

while index < len(data):
    if data[index] == value:
        break
    index += 1
else:
    data.append(value)

print(data)