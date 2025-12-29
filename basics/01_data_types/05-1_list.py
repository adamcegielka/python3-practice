names = ["Adam", "Eve", "John", "Mary", "Michael", "Sophia"]
print(names)

# Add a single name to the list
names.append("David")
print(names)

# Add multiple names to the list
names.extend(["Olivia", "Daniel", "Emma"])
print(names)
print(f"Length of the names list: {len(names)}")

# Remove a name from the list
names.remove("Eve")
print(names)
print(f"Length of the names list after removal: {len(names)}")

print(names[2])  # Accessing the third element - Mary
print(names[-1])  # Accessing the last element - Emma

# Check if a name is in the list
if "John" in names:
    print("John is in the list")
else:
    print("John is not in the list")

if "Eve" in names:
    print("Eve is in the list")
else:
    print("Eve is not in the list")

# Append a list as a single element
names.append(["David", "Olivia", "Daniel", "Emma"])
print(names)  # Note that the last element is a list itself
print(f"Length of the names list after appending a list: {len(names)}")

# Iterate through the list and print each name
for name in names:
    print(name)

# Iterate using index
for index in range(len(names)):
    print(f"Index {index}: {names[index]}")

# Remove the last element which is a list
del names[-1]  # Remove the last element which is a list
print(names)
print(f"Length of the names list after deleting the last element: {len(names)}")

# Delete by index
del names[0]  # Remove by index: Adam
print(names)
print(f"Length of the names list after deleting the first element: {len(names)}")

# Remove by value
names.remove("Michael")  # Remove by value: Michael
print(names)
print(f"Length of the names list after removing Michael: {len(names)}")

# Final iteration to show remaining names
for name in names:
    print(name)

# Demonstrate duplicates and count
names.append("John")  # Add John back to demonstrate duplicates
print(names)

names.count("John")  # Count occurrences of John
print(f"Number of times John appears in the list: {names.count('John')}")

names.remove("John")  # Remove first occurrence of John
print(names)
print(f"Number of times John appears in the list after removal: {names.count('John')}")

# Sort the list
names.sort()
print("Print sorted list", names)

names.sort(reverse=True)
print("Print reverse sorted list", names)   

names[0] = "Aaron"  # Change first element
print("Print list after changing first element", names)

# Clear the list
names.clear()
print("Should print an empty list", names)
print(f"Length of the names list after clearing: {len(names)}")