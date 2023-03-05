#1.
#foreach
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']

for masina in masini:
    print("Masina mea preferata este", masina)

#while
i=0
while i < len(masini):
    print(f'Masina mea preferata este {masini[i]}')
    i+=1

#for
for i in range(len(masini)):
    print(f"Masina mea preferata este{masini[i]}")



#2.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']

#for i in range(len(masini)):
    #masini[i] = masini[i].upper()

print(f"Lista dupa modificare{masini[1:8:1]}")

for i in range(1, len(masini)- 1):
    masini[i] = masini[i].upper()
print(f"Lista dupa modificare{masini}")


#3.

for i in range(len(masini)):
 if masini[i] == "MERCEDES":
    print(f"Am gasit masina dorita de dvs {masini[i]}")
    break
 else:
     print(f'Am gasit masina {masini[i]}. Mai cautam')




#4.nu am rezolvat corect

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']

for i in masini:
          if i == "Trabant" or i == "Lăstun":
              continue
          else:

           print(f"S-ar putea sa va placa masina {i}")



#5.
masini_vechi = [" "]
for masina in masini:
    if masina == "Trabant" or masini == "Lăstun":
        masini.remove("Trabant")
        masini.remove("Lăstun")
        masini_vechi.append("Trabant")
        masini_vechi.append("Lăstun")
        print(f"{masini_vechi}")
print(f"Lista noua de masini este{masini}")

masini_vechi = list()
for i in range(len(masini)):
    if masini[i] ==  "Trabant" or masini == "Lăstun":
        masini_vechi.append(masini_vechi[i])
        masini[i] = 'Tesla'
print(f"Lista noua de masini este{masini}")
print(f'Masini vechi: {masini_vechi}')

#6.
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}

for i in pret_masini.keys():
    if pret_masini[i] < 15000:
     print(f"Pentru un buget de sub 15000 euro puteți alege mașina {i}")



#7.
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
i= 0
for i in range(len(numere)):
    if numere[i] == 3:
        suma = suma + 1
print (f'Cifra 3 apare de {suma} ori')

#2
suma = 0

for numar in numere:
    if numere[i] == 3:
        suma = suma + 1
        print(f"Cifra 3 apare de {numere[i]} ori")




#8.
adunare = 0
for i in numere:
    adunare = adunare +i
    print(f"suma numerelor este: {adunare}")




#9.
cel_mai_mare_nr = None
for numar in numere:
    if cel_mai_mare_nr is None or cel_mai_mare_nr < numar:
        cel_mai_mare_nr = numar
    print(cel_mai_mare_nr)




#10.
numere_modificate = [-abs(numar) for numar in numere]
print(numere_modificate)
numere_modificate = [abs(numar) for numar in numere]
print(numere_modificate)



def convert(numere):
    return[ -i for i in numere ]
print(convert(numere))