import random
import string
import nltk
from nltk.corpus import words

class passwordGenerator:

    def moznosti(self):

        vyber = ""
        while vyber not in ["1","2","3"]:

            vyber = input("Zadej jaký typ hesla chceš vygenerovat:\n1 - Náhodné heslo\n2 - Pin kód\n3 - Heslo z anglických slov\n")

        match(vyber):
            case "1":
                pocetZnaku = int(input("Zadej počet znaků: "))
                hesloRandom = self.randomPassword(pocetZnaku)
                print(hesloRandom)
                

            case "2":

                pocetZnaku = int(input("Zadej počet znaků: "))
                pinRandom = self.randomPin(pocetZnaku)
                print(pinRandom)

            case "3":

                pocetZnaku = int(input("Zadej počet slov: "))
                slovaRandom = self.randomWordPassword(pocetZnaku)
                print(slovaRandom)
            
    
    
    
    def randomPassword(self, lenght):

        hesloList = []
        znakyAll = string.ascii_letters + string.digits + string.punctuation
        
        for x in range(lenght):
            hesloList.append(random.choice(znakyAll))
        
        heslo = ''.join(hesloList)
                
        return heslo

    def randomPin(self, lenght):

        hesloList = []
        znakyAll = string.digits
        
        for x in range(lenght):
            hesloList.append(random.choice(znakyAll))
        
        heslo = ''.join(hesloList)
                
        return heslo

    def randomWordPassword(self, lenght):
        
        hesloList = words.words()  
        slovaAll = random.sample(hesloList, lenght)
        heslo = '-'.join(slovaAll) 

        return heslo



app = passwordGenerator()
app.moznosti()
