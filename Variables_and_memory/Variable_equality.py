
data1 = 100
data2 = 100

print(f"Data1 memory location {id(data1)}.")
print(f"Data2 memory location {id(data2)}.")

# Compare by memory address
print(f"Is data1 located in same memory address than data2 {data1 is data2}.")

# Compare by value
print(f"Is data1  value in same than data2 {data1 == data2}.")
