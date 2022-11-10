import random

zestaw_1 = []
n = int(input("Podaj rozmiar listy: "))
for i in range(n):
    x = random.randint(1, 10)
    zestaw_1.append(x)
print(zestaw_1)


n = int(input("Podaj rozmiar listy: "))
zestaw_2 = [random.randint(5,15) for i in range(n)]
print(zestaw_2)

liczba = int(input("Podaj liczbę: "))
if liczba in zestaw_1:
    print("Liczba z zestawu pierwszego ")
elif liczba in zestaw_2:
    print("Liczba z zestawu drugiego")
else:
    print("Liczba nie znajduje się w żadnym zestawie.")

zestaw_3 = []
zestaw_3 = zestaw_1+zestaw_2
zestaw_3.sort()
print(zestaw_3)