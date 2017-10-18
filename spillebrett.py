from random import randint
from celle import Celle

class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = [[Celle() for _ in range(self._kolonner)] for _ in range(self._rader)]
        self.generasjon = 0
        self.generer()


    def tegnBrett(self):
        for i in range(self._rader):
            for j in range(self._kolonner):
                arg = self._rutenett[i][j].hentStatusTegn()

                print(arg, end="")
            print("")


    def oppdatering(self):
        levende = []
        dodende = []

        self.generasjon += 1

        for i in range(self._rader):
            for j in range(self._kolonner):
                naboliste = self.finnNabo(i, j)
                counter = 0
                for item in naboliste:
                    if item.erLevende():
                        counter += 1

                if (counter < 2) or (counter > 3):
                    dodende.append(self._rutenett[i][j])
                elif (counter == 2) or (counter == 3):
                    levende.append(self._rutenett[i][j])
                else:
                    pass

        for item in levende:
            item.settLevende()

        for item in dodende:
            item.settDoed()


    def finnAntallLevende(self):
        counter = 0
        for i in range(self._rader):
            for j in range(self._kolonner):
                if self._rutenett[i][j].erLevende():
                    counter += 1
        return counter


    def generer(self):
        for i in range(self._rader):
            for j in range(self._kolonner):
                rand = randint(0, 3)
                if rand == 3:
                    self._rutenett[i][j].settLevende()


    def finnNabo (self, rad, kolonne):
        naboliste = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                naboRad = rad+i
                naboKolonne = kolonne+j
                if (naboRad == rad and naboKolonne == kolonne) != True:
                    if (naboRad < 0 or naboKolonne < 0
                            or naboRad > self._rader-1
                            or naboKolonne > self._kolonner-1) != True:
                        naboliste.append(self._rutenett[naboRad][naboKolonne])
        return naboliste



'''
Tester:

TEST = Spillebrett(7, 7)

print("FIRST:")
print("")
print("Antall levende: " + str(TEST.finnAntallLevende()))
print("")

TEST.tegnBrett()
TEST.oppdatering()

print("")
print("Second:")
print("")
print("Antall levende: " + str(TEST.finnAntallLevende()))
print("")

TEST.tegnBrett()
TEST.oppdatering()

print("")
print("THIRD:")
print("")
print("Antall levende: " + str(TEST.finnAntallLevende()))
print("")

TEST.tegnBrett()
TEST.oppdatering()

print("")
print("FOURTH:")
print("")
print("Antall levende: " + str(TEST.finnAntallLevende()))
print("")

TEST.tegnBrett()
'''
