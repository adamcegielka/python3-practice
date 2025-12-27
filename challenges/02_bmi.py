# oblicz wskaźnik BMI (Body Mass Index) na podstawie wzoru:
# BMI = masa (kg) / (wzrost (m))^2
# 1. Zapisz swoją masę w kilogramach do zmiennej weight
# 2. Zapisz swój wzrost w metrach do zmiennej height
# 3. Oblicz wskaźnik BMI i zapisz go do zmiennej bmi
# 4. Pokaż wynik na ekranie używając funkcji print()

weight = 78
height = 1.73
bmi = weight / (height ** 2)

print("My BMI is:", bmi) # My BMI is: 26.061679307694877
print("My BMI is:", round(bmi, 2)) # My BMI is: 26.06
