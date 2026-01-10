# Tuple

# A tuple is an immutable (unchangeable) ordered collection of items.
data = (1, 2, 3, 4, 5)
print(f"Data: {data}")  # Data: (1, 2, 3, 4, 5)
print(type(data))  # <class 'tuple'>
print(f"Tuple length: {len(data)}")  # 5
print(f"First item: {data[0]}")  # First item: 1
print(f"Last item: {data[-1]}")  # Last item: 5
print(f"Slicing (1:4): {data[1:4]}")  # Slicing (1:4): (2, 3, 4)
print(f"Every second item: {data[::2]}")  # Every second item: (1, 3, 5)
print(f"Every fourth item: {data[4:]}") # Every fourth item: (5,)

car = ("Toyota", "Honda", "Ford")
print(f"Car brands: {car}")  # Car brands: ('Toyota', 'Honda', 'Ford')
print(type(car))  # <class 'tuple'>
print(f"Tuple length: {len(car)}")  # 3
print(f"Second car brand: {car[1]}")  # Second car brand: Honda
print(f"Last car brand: {car[-1]}")  # Last car brand: Ford
print(f"Slicing (0:2): {car[0:2]}")  # Slicing (0:2): ('Toyota', 'Honda')
print(f"Every second car brand: {car[::2]}")  # Every second car brand: ('Toyota', 'Ford')
print(f"From second car brand to end: {car[1:]}")  # From second car brand to end: ('Honda', 'Ford')

countries = "USA", "Canada", "Mexico", "Brazil";
print(f"Countries: {countries}")  # Countries: ('USA', 'Canada', 'Mexico', 'Brazil')
print(type(countries))  # <class 'tuple'>
print(f"Tuple length: {len(countries)}")  # 4

# Tuple with a single item
fighters = ("Muhammad Ali",)
print(f"Fighter: {fighters}")  # Fighter: ('Muhammad Ali',)
print(type(fighters))  # <class 'tuple'>
print(f"Tuple length: {len(fighters)}")  # 1

# Empty tuple
names = ()
print(f"Names: {names}")  # Names: ()
print(type(names))  # <class 'tuple'>
print(f"Tuple length: {len(names)}")  # 0

# Tuple concatenation and repetition
num = (1, 2, 3)
numbers = num + (4, 5)
print(f"Numbers: {numbers}")  # Numbers: (1, 2, 3, 4, 5)
print(f"Tuple length: {len(numbers)}")  # 5
repeated = num * 3
print(f"Repeated: {repeated}")  # Repeated: (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(f"Tuple length: {len(repeated)}")  # 9

people = tuple(("Alice", "Bob", "Charlie", "David", "Eve"))
print(f"People: {people}") # People: ('Alice', 'Bob', 'Charlie', 'David', 'Eve')
print(type(people))  # <class 'tuple'>
print(f"Tuple length: {len(people)}")  # 5

# Set
names1 = {"Anna", "Ben"}
names2 = {"Cathy", "David"}
print(names1 | names2)  # {'Anna', 'Cathy', 'David', 'Ben'}
print(names1.union(names2))  # {'Anna', 'Cathy', 'David', 'Ben'}
