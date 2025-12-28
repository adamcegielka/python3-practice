# Check number and print the larger and smaller one

number = input("Enter number from 0 to 10: ")
for i in range(0, 11):
    if number == str(i):
        if i == 10:
            print(f"{number} is the largest number")
            print(f"The smaller number is: {i - 1}")
        elif i == 0:
            print(f"{number} is the smallest number")
            print(f"The larger number is: {i + 1}")
        else:
            print(f"The larger number is: {i + 1}")
            print(f"The smaller number is: {i - 1}")
        break
    if i == 10:
        print("The number is out of range. Please enter a number between 0 and 10.")
        
# run this code in Python: `Ctrl + Fn + F5`
