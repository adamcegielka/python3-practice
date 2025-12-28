# sprawdź czy podane imię jest imieniem męskim, załkładając, że imiona damskie kończą się na "a"

name = input("Enter a name: ")

if name.endswith("a"):
    print(f"{name} is likely a female name.")
else:
    print(f"{name} is a male name.")

# run this code in Python: `Ctrl + Fn + F5`
