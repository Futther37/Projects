# metody pro string: https://www.w3schools.com/python/python_strings_methods.asp

#všechny hodnoty které obsahují E 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newfruit = []
newfruit1 = []

for x in fruits :
    if "e" in x:
        newfruit.append(x)

newfruit1 = [x for x in fruits if "a" in x]

#list []

#tuple ()

#set {}

'''
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print("myfamily")
'''

#výpis pomocí for

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# použití range

for i in range(len(thistuple)):
  print(thistuple[i])

# použití while
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


'''
apple
banana
cherry
'''





#přidání do tuple a změna list/tuple
x = (1,2,3)
x1 = (4,5,6)
x2 = x + x1

y=list(x)

print(x2)

y.append(4)
y.remove(2)

x=tuple(y)

print(y)
print(x)

print(type(x))
print(type(y))



typ = ["red", "big", "tasty"]
ovoce = ["apple", "banana", "cherry"]

for x in typ:
  for y in ovoce:
    print(x, y)
#print(newfruit)
#print(newfruit1)


x = 5

def function(x):
  x = x+10
  return(x)
print(function(x))


'''
#první classa a výpis

class lidi:
  
  idcloveka = 0

  def __init__(self,jmeno,prijmeni,vek):
      lidi.idcloveka += 1
      self.idcloveka = lidi.idcloveka
      self.jmeno = jmeno
      self.prijmeni = prijmeni
      self.vek = vek

  def __str__(self):
     return f"Přihlášený č. {self.idcloveka} je {self.jmeno} {self.prijmeni} s věkem: {self.vek} let."
  
  
clovek1 = lidi("Roman", "Juřena", 26)
clovek2 = lidi("petr", "Novák", 52)
clovek3 = lidi("Luboš", "Tříska", 31)


lidi = [clovek1, clovek2, clovek3]

for clovek in lidi:
    print(clovek)

'''

class Clovek:
    id_cloveka = 0

    def __init__(self, jmeno, prijmeni, vek):
        Clovek.id_cloveka += 1
        self.cislo = Clovek.id_cloveka
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, {self.vek} let"

class Student(Clovek):
    def __init__(self, jmeno, prijmeni, vek, skola):
        super().__init__(jmeno, prijmeni, vek)
        self.skola = skola

    def __str__(self):
        return f"Přihlášený č. {self.cislo} je student {super().__str__()}, škola: {self.skola}"

class Zamestnanec(Clovek):
    def __init__(self, jmeno, prijmeni, vek, firma):
        super().__init__(jmeno, prijmeni, vek)
        self.firma = firma

    def __str__(self):
        return f"Přihlášený č. {self.cislo} je zaměstnanec {super().__str__()}, firma: {self.firma}"

# Seznam osob
lidi = []


while True:
    volba = input("Zadej typ osoby (1 = student, 0 = zaměstnanec, nebo 'konec' pro ukončení): ").lower()

    if volba == "konec":
        break
    elif volba not in ("1", "0"):
        print("❌ Neplatná volba. Zadej 1 pro studenta, 0 pro zaměstnance, nebo 'konec'.\n")
        continue

    jmeno = input("Zadej jméno: ")
    prijmeni = input("Zadej příjmení: ")
    vek = int(input("Zadej věk: "))

    if volba == "1":
        skola = input("Zadej školu: ")
        osoba = Student(jmeno, prijmeni, vek, skola)
    else:  # volba == "0"
        firma = input("Zadej firmu: ")
        osoba = Zamestnanec(jmeno, prijmeni, vek, firma)

    lidi.append(osoba)
    print("✅ Osoba byla úspěšně přidána!\n")

# Výpis všech osob
print("\n📋 Přehled všech přihlášených osob:")
for clovek in lidi:
    print(clovek)





























