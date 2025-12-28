data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Data: {data}")  # Data: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(data))  # <class 'list'>
print(f"List length: {len(data)}")  # 10

# remove one item
data.remove(7)
print(f"Data after removing 7: {data}")  # Data after removing 7: [0, 1, 2, 3, 5, 6, 8, 9]
print(len(data))  # 9

# remove multiple items
for removed_items in [1, 2]:
    data.remove(removed_items)
print(f"Data after removing 1 and 2: {data}")  # Data after removing 1 and 2: [0, 3, 5, 6, 8, 9]
print(len(data))  # 7

if 5 in data:
    print("5 is in the list")  # 5 is in the list
else:
    print("5 is not in the list")

if 7 in data:
    print("7 is in the list")
else:
    print("7 is not in the list")  # 7 is not in the list

for items in list(data):
    print(items)
# Output:
# 0
# 3
# 5
# 6
# 8
# 9

for index in range(len(data)):
    print(f"Index {index}: {data[index]}")
# Output:
# Index 0: 0
# Index 1: 3
# Index 2: 5
# Index 3: 6

for number in data:
    result = number * 2
    print(f"Original: {number} -> multiply : {result}")

# Output:
# Original: 0 -> multiply : 0
# Original: 3 -> multiply : 6
# Original: 5 -> multiply : 10
# Original: 6 -> multiply : 12
# Original: 8 -> multiply : 16
# Original: 9 -> multiply : 18
print(f"End of the test")

# Delete and Remove
cars = ["Toyota", "Honda", "Ford"]
print(type(cars))  # <class 'list'>
print(f"Cars: {cars}")  # Cars: ['Toyota', 'Honda', 'Ford']

# Delete by index
del cars[1] # remove by index: Honda
print(f"Cars after deletion: {cars}")  # Cars after deletion: ['Toyota', 'Ford']

# Remove by value
cars.remove("Ford") # remove by value
print(f"Cars after removing Ford: {cars}")  # Cars after removing Ford: ['Toyota']

# run this code in Python: `Ctrl + Fn + F5`
