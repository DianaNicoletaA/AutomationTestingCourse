# 1
# Instructiunea if reprezinta decizia. Ea executa un cod in caz ca conditia este adevarata si alt cod(cu ajutorul else) in caz ca conditia nu este adevarata.
# IF <conditie>:
# excecuta blocul de cod 1
# ELSE:
# executa blocul de cod 2

# 2.
num = int(input("Va rugam sa introduceti un numar:"))
if num >= 0:
    print("Acesta este un numar natural")
else:
    print("Acesta nu este un numar natural")

# 3.

x = int(input("Va rugam sa introduceti un numar pentru exerciu #3 :"))
if x > 0:
    print("Acesta este un numar pozitiv")
elif x < 0:
    print("Acesta este un numar negativ")
else:
    print("Acesta este un numar neutru")

# 4.

y = int(input("Alegeti un numar intre -2 si 13:"))
if x >= -2 and y <= 13:
    print("Corect")
else:
    print("Eroare")

# 5. Folosesc a si b.

a = int(input("Alegeti un numar:"))
b = int(input("Alegeti al doilea numar:"))
if abs(a - b) < 5:
    print("Adevarat")
else:
    print("Fals")

# 6.  nu sunt sigura daca am rezolvat corect
x_6 = 28

if not x_6 < 5 and not x_6 > 27:

    print("Pass")
else:
    print("eroare")

# 7.
 y_nota_examen = 9
 x_nota_de_trecere = 5
# if x_nota_de_trecere == y_nota_examen:
#     print("Am luat o nota de trecere la examen")
# elif y_nota_examen > x_nota_de_trecere:
#     print("Am trecut examenul cu nota:9")
# else:
#     print("Mai trebuie sa invat la aceasta materie")

if x_nota_de trecere > y_nota_exanen:
    print(f' {x_nota_de_trecere} > {y_nota_examen}')
elif y_nota_examen >x_nota_de_trecere:
    print(f'{y_nota_examen} > {x_nota_de_trecere}')
else:
    print('cele doua valori sunt egale')
# 8.

x_8 = 10
y_8 = 10
z_8 = 8

if x_8 == y_8 or x_8 == z_8:
    print("triunghiul este isoscel")
elif x_8 == y_8 == z_8:
    print("triunghiul este echilateral")
else:
    print("nicio latura nu e egala")

# 9.

litera = input('introdu o litera: ')

if litera.lower() in ('a', 'e', 'i', 'o', 'u', 'ă', ' î ', 'â'):
    print('vocala')
elif litera.upper() in ('A', 'E', 'I', 'O', 'U', 'Ă', 'Î', 'Â'):
    print("Vocala")
else:
    print("Consoana")

litera = input('introdu o litera: ')
string = "aeiouăîâ"
if litera.lower() in string:
    print('vocala')
else:
    print('consoana')

# 10.

nota = int(input("Am luat examenul cu nota: "))


    if nota >=9:
        print("Nota ta este A")
    elif nota >8:
        print("Nota ta este B ")
    elif nota >7:
        print("Nota ta este C")
    elif nota >6:
        print("Nota ta este D")
    elif nota >4:
        print("Nota ta este E")
    else:
        print("Nota ta este F")

