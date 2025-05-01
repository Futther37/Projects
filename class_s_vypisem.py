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
    