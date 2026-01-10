# Tuple representing costs

cost = (100, 200, 300, 400, 500, 600)

for index in range(len(cost)):
    print(f"Spend {index}: {cost[index]}")
# Output:
# Spend 0: 100
# Spend 1: 200
# Spend 2: 300
# Spend 3: 400
# Spend 4: 500
# Spend 5: 600

# policz wydatki za pomocą pętli
total_cost = 0
for amount in cost:
    total_cost += amount
print(f"Total cost: {total_cost}")  # Total cost: 2100

# sprawdź czy kwota 300 jest na liście wydatków
if 300 in cost:
    print("300 is in the cost list")  # 300 is in the cost list
else:
    print("300 is not in the cost list")

# sprawdź czy kwota 700 jest na liście wydatków
if 700 in cost:
    print("700 is in the cost list")
else:
    print("700 is not in the cost list")  # 700 is not in the cost list
    