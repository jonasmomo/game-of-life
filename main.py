from spillebrett import Spillebrett

def main():


while True:
    main()
    rader = int(input("Antall rader: "))
    kolonner = int(input("Antall kolonner: "))

    arg = Spillebrett(rader, kolonner)
    arg.tegnBrett()

    print("Generasjon: " + arg.generasjon)
    print("Antall levende celler: " + arg.finnAntallLevende)
    todo = input("Press enter for aa fortsette. Skriv inn q og trykk enter for aa avslutte: ")