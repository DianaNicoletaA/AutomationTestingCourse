#1.
# O variabila este ca o zona din memoria unui calculator in care stocam o valoare.


#2.
# string

numePrenume = "Diana Aptis"

print(numePrenume)

#int

an_curent = 2023
print(an_curent)

#float

cantitate = 25.5
print(cantitate)

#bloolean

inregistrat = True
(print(inregistrat))


#3.
print(type(numePrenume))

print(type(an_curent))

print(type(cantitate))

print(type(inregistrat))


#4.
r = round(cantitate)
print(r)

# suprasciere

cantitate = '26'
print(cantitate)
print(type(cantitate))

#nu sunt sigura daca am rezolvat bine excerciul nr 4 cu suprascriere.


#5.
print(f'Numele meu este {numePrenume}.')
print(f'Anul {2023} a inceput foarte bine pe plan profesional.')
print(f'Ai nevoie de {cantitate} de grame de faina pentru o briosa.')

assert inregistrat == True, "Nu am inregistrat declaratia."
print ("Am inregistrat declaratia.")

#nu sunt sigura daca am rezolvat corect exercitiul.


#6.
numele = input("Introduce numele tau:")
prenumele = input("Introduce prenumele tau:")

print("Numele meu este " + numele + ";")
print("Prenumele meu este " + prenumele + ".")

x = len(numele) + len(prenumele)

print(f"Numele complet are {x} caractere.")


#7.
lungimea = int(input("Va rugam introduceti lungimea:"))
latimea = int(input("Va rugam introduceti latimea:"))
aria = lungimea*latimea
print(aria)
print(f"Aria dreptunghiului este {aria} centimetri.")


#8.
text_ex8 = "Coral is either the stupidest animal or the smartest rock."
print(text_ex8.count("the"))


#9.
text_ex8 = "Coral is either the stupidest animal or the smartest rock."
print(text_ex8.replace('the', 'THE'))

#10.
text_ex10 = text_ex8.isdigit()
assert text_ex10 == False, "Eroare! Acest string nu contine numere."
print("Am trecut assert-ul.")


