f = open("messagePourSauverLeMonde.txt", "r")
liste_mot = str(f.read()).split(" ")
for i in liste_mot:
    if(i == "volcan"):
        print("A l’aide, tous aux abris !")
        break
f.close()

f = open("livreDeLaNatureEtDesLacs.txt", "r")
liste_mot = str(f.read()).split("\n")
for i in liste_mot:
    if("arbre suspendu" in i):
        print(i)
        break
f.close()
