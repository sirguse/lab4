import random
punkty=[]
ponizej=[]
for x in range(15):
    punkty.append(round(random.uniform(0,50), 2))
print(punkty)
print(f" wartość minimalna: {min(punkty)}")
print(f" wartość minimalna: {max(punkty)}")

liczba = float(input("Podaj liczbe: "))
if liczba in punkty:
    print(punkty.index(liczba))
else:
    print("Nie ma takiej liczby")

suma = sum(punkty)
średnia = round(suma/len(punkty),2)
print(f"Średnia ilość punktów: {średnia}")

for y in punkty:
    if y < średnia:
        ponizej.append(y)

powyzej=[y for y in punkty if y>średnia]
print(f'Osoby ponizej sredniej {ponizej}, osoby powyzej sredniej {powyzej}')