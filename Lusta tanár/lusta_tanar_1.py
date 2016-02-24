import random

osztaly = input("kérném az osztály létszámát!")
osztaly = int(osztaly)

print("Az osztály létszáma: ", osztaly)

osszeg = 0
for x in range(1, osztaly + 1):
    osztalyzat = random.randint(1, 5)
    osszeg = osszeg + osztalyzat
    print(osztalyzat)
    
atlag = osszeg / osztaly
print("átlag: {0:1.2f}".format(atlag))  