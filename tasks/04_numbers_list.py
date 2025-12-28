# wyświetl liczby od 1 do 20 w formie listy
numbers = list(range(1, 21))
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(type(numbers))  # <class 'list'>
print(f"Length of the list: {len(numbers)}")  # 20

# usuń liczby parzyste z listy
for num in list(numbers):
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(f"Length of the list after removing even numbers: {len(numbers)}")  # 10

# sprawdź czy liczba 10 jest na liście
if 10 in numbers:
    print("10 is in the list")
else:
    print("10 is not in the list")  # 10 is not in the list

# sprawdź czy liczba 15 jest na liście
if 15 in numbers:
    print("15 is in the list")  # 15 is in the list
else:
    print("15 is not in the list")
