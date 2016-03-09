összeg = int(input("Add meg a kezdő összeget!"))
kamat = float(input("Adja meg a kamatot!"))
evek = int(input("Adja meg az évek számát!"))

eredmeny = összeg
for i in range(1, evek+1):
    eredmeny = eredmeny * kamat + eredmeny
    
print("A kamatos kamat: ", eredmeny)
