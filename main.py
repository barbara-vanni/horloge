import time
import keyboard


def afficher_heure(heure, format_12h=False):
    if format_12h:
        heure_format = "{:02d}:{:02d}:{:02d} {}".format(heure[0] % 12 or 12, heure[1], heure[2], "AM" if heure[0] < 12 else "PM")
    else:
        heure_format = "{:02d}:{:02d}:{:02d}".format(heure[0], heure[1], heure[2])
    print(heure_format, end='\r')


def regler_alarme(heures, minutes, secondes):
    alarme = (heures, minutes, secondes)
    return alarme


def pause():
    return keyboard.is_pressed("p")


# ligne pour régler l'heure de l'alarme
alarme_set = regler_alarme(15,5,0)
en_pause = False


def main():
    format_heure = input("Utiliser le format 12h ? (oui/non) : ")
    heures = int(input("Entrez l'heure de départ (hh) : "))
    minutes = int(input("Entrez les minutes de départ (mm) : "))
    secondes = int(input("Entrez les secondes de départ (ss) : "))

    heure_actuelle = (heures, minutes, secondes)

    try:
        while True:
            if pause():
                print("Horloge en pause. Appuyez sur 'b' pour reprendre.")
                while not keyboard.is_pressed("b"):
                    pass
                print("Reprise de l'horloge.")

            if format_heure == "oui" or format_heure == "Oui":
                afficher_heure(heure_actuelle, True)
            else:
                afficher_heure(heure_actuelle, False)

            time.sleep(1)

            heure_actuelle = (heure_actuelle[0], heure_actuelle[1], heure_actuelle[2] + 1)
            if heure_actuelle[2] >= 60:
                heure_actuelle = (heure_actuelle[0], heure_actuelle[1] + 1, 0)
                if heure_actuelle[1] >= 60:
                    heure_actuelle = (heure_actuelle[0] + 1, 0, 0)
                    if heure_actuelle[0] >= 24:
                        heure_actuelle = (0,0,0) 
            
            if heure_actuelle == alarme_set:
                print(*heure_actuelle,"It's time. Wake up !")
            

    except KeyboardInterrupt:
        print("\nProgramme arrêté.")

main()


