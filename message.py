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


# 2

f = open("lafamilleDodo.txt", "r")
liste_num = str(f.read()).split(",")
temp_list = []

for i in liste_num:
    if i not in temp_list:
        temp_list.append(i)

liste_num = temp_list
for i in range(len(liste_num)):
    liste_num[i] = int(liste_num[i])
print("\nListe des ages triées, sans doublons :",sorted(liste_num))
f.close()


f = open("ageDodo.txt", "r")
liste_ages = str(f.read()).split(", ")
mineurs, majeurs = 0,0
for i in liste_ages:
    i = int(i)
    if i >= 5:
        majeurs += 1
    else :
        mineurs += 1
print("\nIl y a",mineurs,"mineurs et", majeurs, "majeurs.")
