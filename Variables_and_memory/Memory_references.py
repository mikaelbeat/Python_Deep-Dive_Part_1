
import sys, ctypes

data = 10

print(f"Memory address for variable is {id(data)}.")
print(f"Memory address for variable in hexadesimal is {hex(id(data))}.")

print("\n****************************************\n")


list = [1, 2, 3]

print(f"Amount of references to variable list {sys.getrefcount(list) - 1}.")

def count_references(address: int):
    return ctypes.c_long.from_address(address).value


print(f"Counting references using ctypes {count_references(id(list))}.")
