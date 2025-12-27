# Obliczenia na łańcuchach znaków (stringach)

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full Name:", full_name)  # Full Name: John Doe

# Konkatenacja łańcuchów znaków
greeting = "Hello, " + full_name + "!"
print(greeting)  # Hello, John Doe!

# Powielenie łańcucha znaków
laugh = "Ha" * 3
print(laugh)  # HaHaHa

# Długość łańcucha znaków
length = len(full_name)
print("Length of Full Name:", length)  # Length of Full Name: 8

# Indeksowanie i wycinanie (slicing)
first_letter = full_name[0]
print("First Letter:", first_letter)  # First Letter: J

substring = full_name[1:4]
print("Substring (1-4):", substring)  # Substring (1-4): ohn

# Metody łańcuchów znaków
upper_name = full_name.upper()
print("Uppercase Full Name:", upper_name)  # Uppercase Full Name: JOHN DOE

lower_name = full_name.lower()
print("Lowercase Full Name:", lower_name)  # Lowercase Full Name: john doe

split_name = full_name.split(" ")
print("Split Name:", split_name)  # Split Name: ['John', 'Doe']

replace_name = full_name.replace("Doe", "Smith")
print("Replaced Name:", replace_name)  # Replaced Name: John Smith

# /newline and \t tab characters
multiline_string = "Hello,\nThis is a multiline string.\n\tIt has tabs."
print(multiline_string)
# Output:
# Hello,
# This is a multiline string.
#     It has tabs.

# Run this code in Python: `Ctrl + Fn + F5`
