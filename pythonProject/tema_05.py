#1.

def suma_numere():
    a = 50
    b = 70
    suma = a + b
    print(f'Suma este {suma}')

suma_numere()


def suma(x,y):
    rezultat = x+y
    print(x,"+",y,"=",rezultat)

n1 = int(input("Intoduceti un numar: "))
n2 = int(input("Intdoceti al dolea numar: "))

suma(n1,n2)

def suma(x,y):
    z=x+y
    return z
x=int(input("Primul nr este:"))
y=int(input("Al doilea numar este:"))

z=suma(x,y)
print(f"suma numerelor este:{z}")

#2.

def numar_par(n):
    return n % 2 == 0
def numar_impar(n):
    return n % 2 !=0

print(numar_par(10))
print(numar_impar(6))
def numar_par(n):
    return n % 2 == 0
def numar_impar(n):
    return n % 2 !=0

print(numar_par(67))
print(numar_impar(68))

#3

def suma_caractere_litere(nume):
    litera = 0
    for i in str:
        litera += 1
#nu stiu cum sa scad spatiile

nume = "Aptis Diana Nicoleta"
spatii = nume.count(' ')
caractere = len(nume) - spatii


print(f"Numele meu are {caractere} caractere.")

#4.

def aria_dreptunghiului():
    lun = int(input("Introduceti lungimea dreptunghiului:"))
    lat = int(input("Introduceti latimea dreptunghiului:"))
    arie = lun * lat
    return arie
print(f" Aria dreptunghiului este = {aria_dreptunghiului()}")

#5.

def aria_cercului(raza):
    arie = raza**2*math.pi
    return arie
raza = float(input("Introduceti raza:"))
print("Aria cercului este:", aria_cercului(raza))


#6.
def verificare(a,functie):
    rezultat = []
    for i in functie:
        if i in a:
            rezultat.append("True")
        else:
            rezultat.append("False")
    return rezultat
a = "Luna viitoare voi incepe un job nou."
functie = [ 'a', 'b','c', 'd']
print(verificare(a,functie))

#7
def litere(text):
    adunare = {"litere_mici":0, "litere_mari":0}
    for litera in text:
        if litera.isupper():
            adunare["litere_mici"] +=1
        elif litera.islower():
            adunare["litere_mari"] +=1
        else:
            pass

    print("Textul contine:", adunare["litere_mici"])
    print("Textul contine:", adunare["litere_mari"])
litere("Acesta Este Un Test")

#8

def lista_numere_pozitive(lista):
    lista_numere = list([])
    for i in range(len(lista)):
        if (lista[i]) >0:
            lista_numere.append((lista[i]))

    return lista_numere
test_lista = [2,56,-78,-89,563]
lista_numere =lista_numere_pozitive(test_lista)
print(lista_numere)

#9
def exercitiu_numere():
    x = 67
    y = 78
    if x > y:
     print(f"Primul numar este mai mare decat al doilea.")
    elif x ==y:
         print(f"Numerele sunt egale.")
    else:
        print(f"Al doilea numar este mai mare decat primul.")

exercitiu_numere()


#10 #aici nu returneaza cu true, sau false. este ceva gresit

def exercitiu(numar,set):
    i=0

    if numar not in set:
        set.add(numar)
        print("am adaugat numărul nou în set")
        return True
    else:
        print("nu am adaugat numărul în set. Acesta există deja")
        return False
numar = int(input("Introduceti un numar"))
set = {4,6,7,8}

exercitiu(numar,set)
