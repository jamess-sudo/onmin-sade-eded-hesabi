#yazilan ilk 10000 sade ededin 3 le baslayib 7 ile bitenlerini capa versin

onminlik=list()

sayi=3

while True:
    prime=True

    for i in range(2, int(sayi**0.5)+1):

        if sayi%i==0:
            prime=False
            break

    if prime:
        onminlik.append(sayi)
        if len(onminlik)==10000:
            break

    sayi +=1

list2=[]

for sade in onminlik:
    strSade=str(sade)

    if strSade.startswith("3") and strSade.endswith("7"):
        list2.append(sade)

print(list2)
print(len(list2))
    