
for a , b in [(1, 2), (3, 4), (5, 6)]:
    print(f"First value -> {a}, Second value -> {b}")


print("\n********************\n")

for i in range(5):
    if i == 3:
        continue # when value is 3 doens't print value, jumps back to start of the loop 
    print(i)


print("\n********************\n")

for i in range(5):
    if i == 3:
        break  # when value is 3 exits the loop
    print(i)


print("\n********************\n")


data = "Hello"

for i, c in enumerate(data):
    print(i, c)