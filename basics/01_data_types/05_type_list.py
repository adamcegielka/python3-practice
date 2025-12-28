# Type List
# W Pythonie lista to uporządkowana kolekcja elementów, które mogą być różnych typów danych. Listy są definiowane za pomocą nawiasów kwadratowych [] i elementy są oddzielone przecinkami.

# Przykład tworzenia listy
fruits = ["apple", "banana", "cherry"]

print("Fruits List:", fruits)  # Fruits List: ['apple', 'banana', 'cherry']
print(f"Fruits List: {fruits}")  # Fruits List: ['apple', 'banana', 'cherry']

# Dostęp do elementów listy za pomocą indeksów
first_fruit = fruits[0]
print("First Fruit:", first_fruit)  # First Fruit: apple
print(f"First Fruit: {first_fruit}")  # First Fruit: apple

last_fruit = fruits[-1]  # cherry
print(f"Last Fruit: {last_fruit}")  # Last Fruit: cherry

# Modyfikacja elementów listy
fruits[1] = "blueberry"
print("Updated Fruits List:", fruits)  # Updated Fruits List: ['apple', 'blueberry', 'cherry']

# Dodawanie elementów do listy
fruits.append("date")
print("Fruits List after append:", fruits)  # Fruits List after append: ['apple', 'blueberry', 'cherry', 'date']

# Usuwanie elementów z listy
fruits.remove("cherry")
print("Fruits List after removal:", fruits)  # Fruits List after removal: ['apple', 'blueberry', 'date']

# Długość listy
length = len(fruits)
print("Length of Fruits List:", length)  # Length of Fruits List: 3

# Iteracja przez listę
print("Iterating through Fruits List:")
for fruit in fruits:
    print(fruit)
# Output:
# apple
# blueberry
# date

# Ćwiczenie:
# 1. Utwórz listę z nazwami trzech swoich ulubionych filmów.
# 2. Dodaj do listy czwarty film.
# 3. Usuń drugi film z listy.
# 4. Wyświetl ostateczną listę filmów oraz jej długość
favorite_movies = ["Inception", "The Matrix", "Interstellar"]
favorite_movies.append("The Dark Knight")
favorite_movies.remove("The Matrix")
print(f"Favorite Movies: {favorite_movies}")  # Favorite Movies: ['Inception', 'Interstellar', 'The Dark Knight']
print(f"Number of Favorite Movies: {len(favorite_movies)}")  # Number of Favorite Movies: 3

new_movies = ["Pulp Fiction", "Forrest Gump"]
favorite_movies.extend(new_movies)
print(f"Updated Favorite Movies: {favorite_movies}")  # Updated Favorite Movies: ['Inception', 'Interstellar', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump']
print(len(favorite_movies))  # 5

# Str and Int
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
print(type(names))  # <class 'list'>
print(type(ages))   # <class 'list'>
print(f"Names: {names}")  # Names: ['Alice', 'Bob', 'Charlie']
print(f"Ages: {ages}")    # Ages: [25, 30, 35]

names_ages = ["Alice", 25, "Bob", 30, "Charlie", 35]
print(f"Names and Ages: {names_ages}")  # Names and Ages: ['Alice', 25, 'Bob', 30, 'Charlie', 35]
print(f"Fist Person: {names_ages[0]}, Age: {names_ages[1]}")  # Fist Person: Alice, Age: 25
print(f"Last Person: {names_ages[-2]}, Age: {names_ages[-1]}")  # last Person: Charlie, Age: 35

print(len(names_ages))  # 6
print(names_ages[5])  # 35
print(names_ages[len(names_ages)-1])  # 35

print( 30 in names_ages)  # True
print( "David" in names_ages)  # False

for item in list(names_ages):
    print(item)
# Output:
# Alice
# 25
# Bob
# 30
# Charlie
# 35

data = [
    ["Alice", 25],
    ["Bob", 30],
    ["Charlie", 35]
]
print(f"Data: {data}")
# Data: [['Alice', 25], ['Bob', 30], ['Charlie', 35]]
print(len(data))  # 3
print(data[1])  # ['Bob', 30]
print(data[1][0])  # Bob
print(data[1][1])  # 30

# Run this code in Python: `Ctrl + Fn + F5`
