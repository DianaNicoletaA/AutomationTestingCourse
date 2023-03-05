from abc import abstractmethod, ABC

# Abstaction
class FormaGeometrica(ABC):
    PI = 3.14
    @abstractmethod
    def aria(self):
        pass
    def descriere(self):
        print("Cel mai probabil am colturi.")

#Inheritance
class Patrat(FormaGeometrica):
    __latura = None

   # def __init__(self, latura):
   #   self.latura = latura

    def aria(self):
        return self.__latura * self.__latura

    # Encapsulation
    def set_latura(self,latura):
        if latura <= 0:
            print("Latura nu paote fi negativa")
        else:
             self.__latura = latura
    def get_latura(self):
        return self.__latura
    def delete_latura(self):
        del self.__latura



p1 = Patrat()
p1.set_latura(8)
aria_p1 = p1.aria()
print(f'Aria patratului este {aria_p1}')

latura_pi = p1.get_latura()

print(f"Latura patratului p1: {p1.get_latura()}")

p1.descriere()
class Cerc(FormaGeometrica):
    __raza = None

    def __init__(self, raza_cercului):
        self.__raza = raza_cercului

    def get_raza(self):
        return self.__raza
    def set_raza(self, raza2):
        if raza2 <=0:
            print("Raza este prea mica.")
        else:
            self.__raza = raza2
    def delete_raza(self):
        del self.__raza

    def aria(self):
        return self.PI * self.__raza * self.__raza

    def descriere(self):
        print("Eu nu am colturi.")

c1 = Cerc(6)
c1.descriere()
print(f"Aria cercului este {c1.aria()}")
