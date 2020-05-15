
min_length = 2

# isprintable() checks is value printable. Cat is and \nCat is not.
# isalpha() checks is all characters in the string alphabets. Cat is and Cat9 is not.

while True:
    name = input("Please, enter you name: ")
    if (len(name) >= min_length and name.isprintable() and name.isalpha()):
        break

print(f"Hello {name}, you are now logged to system.")
