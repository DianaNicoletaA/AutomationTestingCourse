#1.
note_muzicale = ["do", "re", "mi","fa", "sol", "la", "si", "do"]
print(f"Lista cu notele muzicale este: {note_muzicale}")
note_muzicale.reverse()
print(f'lista inversata este: {note_muzicale}')


#2.
print(note_muzicale.count("do"))

#3.
#varianta 1
lista_1 = ["3","1","0","2"]
lista_2 =["6","5","4"]
lista_unita = lista_1 + lista_2
print(f"Lista unita este: {lista_unita}")

#varianta_2
lista_1.extend(lista_2)
print(f"Lista dupa extend {lista_1}")

#4.
lista_1.sort()
print(f"Lista dupa sort: {lista_1}")

lista_1.remove("0")
print(f"lista dupa stergerea cifrei 0: {lista_1}")

#5.
if len(lista_unita) == 0:
 print("list este goala")
else:
 print("Lista nu este goala")

#6.
lista_unita.clear()
print(f"Lista dupa apelarea metodei clear este: {lista_unita}")

#7.
if len(lista_unita) == 0:
 print("Lista este goala")
else:
 print("Lista nu este goala")

#8.
dict1 = {'Ana': 8, 'Gigel' : 10, 'Dorel' : 5}
print(f"Elevii sunt: {dict1.keys()}")

#9.
print("Ana a luat nota:", dict1["Ana"])
print("Gigel a luat nota:", dict1["Gigel"])
print("Dorel a luat nota:", dict1["Dorel"])

#10.
dict1.update({"Dorel" : 6})
print("Dupa contestatie, Dorel, a luat nota : ", dict1["Dorel"])

#11.
dict1.pop("Gigel")
dict1["Ionica"] = 9
print(f"Noul dictioar este {dict1}")

#12.
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(f'Setul updatat este: {zile_sapt}')
#setul nu poate contine un duplicat de elemente

#13.
if weekend.issubset(zile_sapt):
    print(True)
else:
    print(False)

if not weekend == zile_sapt:
    print(True)
else:
    print(False)

#14.
diferenta = zile_sapt - weekend
print(f'Diferenta este:  {diferenta}')

weekend.symmetric_difference(zile_sapt)
print(f'symetric difference: {weekend}')


#15.
intersectia_elementelor = zile_sapt.intersection(weekend)
print(intersectia_elementelor)