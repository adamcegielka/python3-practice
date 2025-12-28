# wyświetl wszystkie liczby pierwsze od 1 do 100

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primes = []
for number in range(1, 101):
    if is_prime(number):
        primes.append(number)

print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(f"Length of the prime numbers list: {len(primes)}")  # 25
