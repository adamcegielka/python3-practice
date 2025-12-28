# 10. Stwórz grę, w której wylosujesz liczbę z przedziału
# 1 - 100, zapiszesz tę liczbę do zmiennej, a następnie 
# poprosisz użytkownika o odgadnięcie tej liczby. Po każdej 
# próbie wyświetlaj informację, czy liczba podana przez 
# użytkownika jest mniejsza czy większa od wylosowanej.
# Gdy użytkownik odgadnie liczbę, zakończ grę i 
# wyświetl liczbę prób, które były potrzebne do odgadnięcia liczby.

import random
number_to_guess = random.randint(1, 100)
attempts = 0
while True:
    user_guess = int(input("Guess the number (between 1 and 100): "))
    attempts += 1
    if user_guess < number_to_guess:
        print("Your guess is too low. Try again.")
    elif user_guess > number_to_guess:
        print("Your guess is too high. Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        break

# run this code in Python: `Ctrl + Fn + F5`
