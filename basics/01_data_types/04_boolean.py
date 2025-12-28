# Boolean
# In Python, the Boolean data type has two values: True and False.

is_sunny = True
is_raining = False
print("Is it sunny?", is_sunny)      # Output: Is it sunny? True
print("Is it raining?", is_raining)  # Output: Is it raining? False

# Boolean operations
a = 10
b = 20
print("a < b:", a < b)   # Output: a < b: True
print("a > b:", a > b)   # Output: a > b: False
print("a == b:", a == b) # Output: a == b: False
print("a != b:", a != b) # Output: a != b: True

# Logical operations
is_adult = True
has_id = False

can_enter = is_adult and has_id
print("Can enter:", can_enter)  # Output: Can enter: False

can_buy = is_adult or has_id
print("Can buy:", can_buy)      # Output: Can buy: True

not_adult = not is_adult
print("Not adult:", not_adult)  # Output: Not adult: False

# Run this code in Python: `Ctrl + Fn + F5`
