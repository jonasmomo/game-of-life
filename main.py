from spillebrett import Spillebrett

def main():

    rader = int(input("Antall rader: "))
    kolonner = int(input("Antall kolonner: "))

    arg = Spillebrett(rader, kolonner)
    arg.tegnBrett()

    todo = True
    while todo:


        print("Generasjon: " + str(arg.generasjon))
        print("Antall levende celler: " + str(arg.finnAntallLevende()))

        action = input("Press enter for aa fortsette. Skriv inn q og trykk enter for aa avslutte: ")

        if action == "q":
            break
        elif action == "":
            arg.oppdatering()
            arg.tegnBrett()
        else:
            print("hei")

main()
