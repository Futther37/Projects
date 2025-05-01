import random

class hra:
    moznosti = ["kámen","nůžky", "papír"]
    podminka = {
        "kámen" : "nůžky",
        "nůžky" : "papír",
        "papír" : "kámen"
    }

    def __init__(self):
        self.bodyHrac = 0
        self.bodyPc = 0

    def volbaHrace(self):
        hracVolba = input("zadej svou volbu: kámen, nůžky, papír (pro ukončení zadej 'Q'): ").lower()

        while hracVolba not in self.moznosti and hracVolba != "q":
            hracVolba = input("zadej svou volbu: kámen, nůžky, papír (pro ukončení zadej 'Q'): ").lower()

        if hracVolba == "q":
            print("konec hry")
            return "q"
            
        return hracVolba
                
    def volbaPc(self):
        pcVolba = random.choice(self.moznosti)
        return pcVolba
    
    def kdoVyhral(self, hracVolba, pcVolba):
        if hracVolba == pcVolba:
            return "Je to remíza"
        
        elif self.podminka[hracVolba] == pcVolba:
            self.bodyHrac += 1
            return "Vyhrál jsi"
        
        else:
            self.bodyPc +=1
            return "prohrál jsi"


moje_hra = hra()

while True:
    hrac_volba = moje_hra.volbaHrace()

    if hrac_volba == "q":
        break
    
    pc_volba = moje_hra.volbaPc()

    vysledek = moje_hra.kdoVyhral(hrac_volba, pc_volba)
    
    print(f"PC si vybral: {pc_volba}")
    print(vysledek)
    print(f"skóre: Hráč {moje_hra.bodyHrac}:{moje_hra.bodyPc} PC")

