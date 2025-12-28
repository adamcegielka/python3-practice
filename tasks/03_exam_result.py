# Napisz program, który zapyta użytkownika o wynik 
# # na egzaminie (od O do 100) i wyświetli odpowiednią ocenę:
# 90 - 100 -> 5
# 80 - 89 -> 4
# 70 - 79 -> 3
# 60 - 69 -> 2
# poniżej 60 -> 1

score = int(input("Enter your exam score (0-100): "))
if 90 <= score <= 100:
    grade = 5
elif 80 <= score < 90:
    grade = 4
elif 70 <= score < 80:
    grade = 3
elif 60 <= score < 70:
    grade = 2
elif 0 <= score < 60:
    grade = 1
else:
    grade = None
    print("Invalid score. Please enter a number between 0 and 100.")
if grade is not None:
    print(f"Your grade is: {grade}")

# run this code in Python: `Ctrl + Fn + F5`
