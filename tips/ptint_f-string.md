# Porównanie metod zapisu (Ewolucja)

| Metoda | Przykład kodu | Czytelność | Zalecenie |
| --- | --- | --- | --- |
| **f-string (od 3.6+)** | `print(f"Cześć {name}!")` | ⭐⭐⭐⭐⭐ | **Używaj zawsze** |
| **.format()** | `print("Cześć {}!".format(name))` | ⭐⭐⭐ | Tylko dla starych wersji |
| **Operator %** | `print("Cześć %s!" % name)` | ⭐⭐ | Nie używaj (przestarzałe) |
| **Przecinki** | `print("Cześć", name, "!")` | ⭐ | Tylko do szybkich testów |

---

### Czym są f-stringi?

**f-stringi** (Formatted String Literals) to najnowocześniejszy sposób tworzenia napisów w Pythonie. Pozwalają one na bezpośrednie „wstrzykiwanie” wartości zmiennych lub wyników działań do wnętrza tekstu.

#### Najważniejsze cechy:

* **Znak `f`:** Musi znaleźć się bezpośrednio przed cudzysłowem (np. `f"..."`).
* **Klamry `{ }`:** Wszystko, co umieścisz wewnątrz klamer, zostanie obliczone przez Pythona i zamienione na tekst.
* **Automatyczna konwersja:** Nie musisz martwić się o typy danych – Python sam zamieni liczbę (`int`) czy listę na tekst, aby pasowały do zdania.

#### Przykłady zastosowania:

1. **Podstawowe wstawianie:**
```python
user = "Adam"
print(f"Witaj, {user}!") 
# Wynik: Witaj, Adam!

```

2. **Działania w locie:**
```python
cena = 100
print(f"Cena z VAT: {cena * 1.23}")
# Wynik: Cena z VAT: 123.0

```

3. **Szybkie sprawdzanie zmiennych (Debugowanie):**
```python
x = 10
print(f"{x=}") 
# Wynik: x=10 (bardzo pomocne przy szukaniu błędów!)

```
