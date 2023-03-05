#1.
class Cerc:
#constructor

    def __init__(self,raza,culoare):
        self.raza = raza
        self.culoare = culoare
#metode
    def descriere_cerc1(self):

       print(f'Cercul are culoarea {self.culoare} si raza de {self.raza} cm')

    def arie_cerc(self):
         return 3.14 * (self.raza **2)

    def diametru_cerc(self):
          return 2 * self.raza

    def circumferinta(self):
        return 2 * 3.14 * self.raza
    def perimetru(self):
        return 2* 3.14 * self.raza

#obiecte
cerc1 = Cerc(7,"verde")
cerc2 = Cerc(9,"roz")

print(cerc1.raza)
print(cerc2.raza)

print(cerc1.culoare)
print(cerc2.culoare)


print(cerc1.perimetru())
print(cerc2.perimetru())

print(cerc1.arie_cerc())
print(cerc2.arie_cerc())


print(cerc1.diametru_cerc())
print(cerc2.diametru_cerc())

print(cerc1.circumferinta())
print(cerc2.circumferinta())

#2.

class Dreptunghi:
#constructor

    def __init__(self,lungime,latime,culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare



#metode
    def descrie(self):
        print(f"Dreptunghiul are culoarea {self.culoare}, latimea {self.latime} si lungimea {self.lungime}")

    def arie_d(self):
        return self.lungime * self.latime

    def perimetru_d(self):
        return 2 * self.lungime + 2 * self.latime
    #def culoare_noua(self):
        # nu stiu cum sa schimb culoarea cu parametrii


# obiecte si atributele

d1 = Dreptunghi(5, 4, "galben")
d2 = Dreptunghi(3, 6, "mov")
Dreptunghi.descrie(d1)
Dreptunghi.descrie(d2)
print(d1.arie_d())
print(d2.arie_d())

print(d1.perimetru_d())
print(d2.perimetru_d())
#schimba_culoarea
d1.culoare = "rosie"
Dreptunghi.descrie(d1)

#3.
class Angajat:
    def __init__(self, nume,prenume,salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
         print(f'Angajatul,{self.nume} {self.prenume} are salariul {self.salariu} lei')

    def nume_complet(self):
        return "{} {}".format(self.nume,self.prenume)

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu_procent(self):
        return 100/10

ang1 = Angajat("Dua","Lipa", 9000)
ang2 = Angajat("Kanye","West", 8000)

Angajat.descrie(ang1)
Angajat.descrie(ang2)
Angajat.nume_complet(ang1)
Angajat.nume_complet(ang2)
print(Angajat.nume_complet(ang1))
print(Angajat.nume_complet(ang2))
print(Angajat.salariu_lunar(ang1))
print(Angajat.salariu_lunar(ang2))
print(Angajat.salariu_anual(ang1))
print(Angajat.salariu_anual(ang2))
print(Angajat.marire_salariu_procent(ang1))

"""
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
"""
#4. #aici nu mi-a calculat creditarea soldului cu noul sold, trebuia sa il supra-scriu banuiesc.

class Cont:
    plati = 4563
    incasare = 3440

    def __init__(self,iban,titular_cont,sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei")

    def debitare_cont(self):

        return self.sold - self.plati

    def creditare_cont(self):

        return self.sold + self.incasare

titular1 = Cont("RO12467", "Maria Manole", 6743)
titular2 = Cont("R034556", "Petre Patraru", 4663)
Cont.afisare_sold(titular1)
Cont.afisare_sold(titular2)

print(Cont.debitare_cont(titular1))
print(Cont.debitare_cont(titular2))

print(Cont.creditare_cont(titular1))
print(Cont.creditare_cont(titular2))

