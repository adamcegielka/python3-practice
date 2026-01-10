# Variables Declaration in Python
# In Python, variables are created when you assign a value to them.

# Example of declaring variables
age = 25                 # Integer
name = "Adam"            # String
height = 5.7             # Float
is_student = True        # Boolean

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

print(age + 2)
print(name + " Smith")
print(name + " is " + str(age) + " years old.")

number1 = 10
number2 = 20
sum_result = number1 + number2
print("Sum:", sum_result)

# Run this code in Python: `Ctrl + Fn + F5`

"""
comment:
This code snippet demonstrates how to declare and manipulate variables in Python. 
It creates variables to store details
"""

# Specify the data type of a variable
weight: float = 70.5  # Float type
is_employed: bool = False  # Boolean type
print("Weight:", weight)
print("Is Employed:", is_employed)

x = str(3)
print(x) # x will be '3'
print(type(x)) # x is of type str

y = int(3)
print(y) # y will be 3
print(type(y)) # y is of type int

z = float(3)
print(z) # z will be 3.0
print(type(z)) # z is of type float

# Ten zapis nie tworzy typu, tylko opisuje, jakiego typu powinna być zmienna.
weight: float = 70.5

# Tworzy zmienną typu float, tworzy floata w czasie działania programu.
z = float(3)
