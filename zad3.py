zwierzeta = []
for i in range(4):
    s = input("Podaj zwierzeta: ")
    zwierzeta.append(s)
zwierzeta.sort()
print(zwierzeta[0], zwierzeta[-3:], len(zwierzeta))
