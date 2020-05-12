
value1 = 0
value2 = 2

while value1 < 4:
    print("--------------------------")
    value1 += 1
    value2 -= 1

    try:
        value1 / value2
    except ZeroDivisionError:
        print(f"Division by zero! Tried to divide {value1} using {value2}.")
        continue
    finally:
        print(f"Value1 is {value1} and value2 {value2}.")

    print(f"Main loop, value1 {value1},  value2 {value2}.")
else:
    print("Code executed without zero division error.")