from os import name


f = open("messagePourSauverLeMonde.txt", "r")
liste_mot = str(f.read()).split(" ")
for i in liste_mot:
    if(i == "volcan"):
        print("A l’aide, tous aux abris !")
        break
f.close()

f = open("livreDeLaNatureEtDesLacs.txt", "r")
liste_phrase = str(f.read()).split("\n")
for i in liste_phrase:
    if("arbre suspendu" in i):
        print(i)
        break
f.close()

f = open("desProjectilesEtDesDodos.txt", "r")
liste_mot = str(f.read()).split(" ")
pas_gauche,pas_droite,pas_avant = 0,0,0
for i in liste_mot:
    if "rocher" in i:
        pas_gauche += 5
    if "dodo" in i:
        pas_droite += 6
    if "arbre" in i:
        pas_avant += 10
    sum = int(pas_gauche+pas_droite+pas_avant)
    if sum >= 100 and "lac" in i:
        print("\nPas en tout :",sum)
        max = pas_gauche
        name_max = "Vers la gauche"
        if pas_droite > max:
            max = pas_droite
            name_max = "Vers la droite"
        if pas_avant > max:
            max = pas_avant
            name_max = "Vers l'avant"
        print("\nDirection dans laquelle vous avez fait le plus de pas :", name_max)
f.close()
