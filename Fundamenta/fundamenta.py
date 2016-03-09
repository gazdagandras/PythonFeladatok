osszeg = int(input("Adja meg a havi befizetett összeget!"))
evek = int(input("Adja meg az évek számát!"))
kamat = 1.3
honapok = int(12)

for i in range (1, evek+1):
    eredmeny = osszeg * honapok * kamat * evek
    
print(eredmeny)
    

