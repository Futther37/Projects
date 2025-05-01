import random

bodyHrac = 0
bodyPc = 0
moznosti = ["kámen","nůžky", "papír"]
podminka = {
    "kámen" : "nůžky",
    "nůžky" : "papír",
    "papír" : "kámen"
}

while True:
    volbaHrace = input("zadej svou volbu: kámen, nůžky, papír: (Q pro ukončení)").lower()

    if volbaHrace == "q":
        print("díky za hru")
        break

    while volbaHrace not in moznosti:
        volbaHrace = input("zadej svou volbu: kámen, nůžky, papír: ").lower()

    volbaPc = random.choice(moznosti)

    print(f"Tvá volba: {volbaHrace}\nvolba pc: {volbaPc}")

    if volbaHrace == volbaPc:
        print("Je to remíza")
    elif podminka[volbaHrace] == volbaPc:
        bodyHrac += 1
        print("Vyhrál jsi!!")
    else:
        bodyPc += 1
        print("Prohrál jsi")

    print(f"Skóre Hráč: {bodyHrac} : {bodyPc} PC")

