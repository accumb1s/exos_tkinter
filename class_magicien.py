import class_perso as cp

class Race:
    def __init__(self, type, langue):
        self.type = type
        self.langue = langue
        print(type, langue)

class Magicien(cp.Personnage):
    def __init__(self, vie, nom, force,
                 endurance,
                 rapidite,
                 intelligence,
                 pointsDeMagie,
                 race,
                 img_path):
        super().__init__(vie,
                         nom,
                         force,
                         endurance,
                         rapidite,
                         intelligence,
                         img_path)
        self.pointsDeMagie = pointsDeMagie
        self.race = race

    def afficheCaracteristiquesMagicien(self):
        caract = (f"{self.nom} a une force de {self.force}\n"
                  f"une endurance de {self.endurance}\n"
                  f"une rapidite de {self.rapidite}\n"
                  f"une intelligence de {self.intelligence}\n"
                  f"et Il reste à {self.nom} "
                  f"{self.pointsDeMagie} points de magie\n")
        print(caract)
        return caract

    def faireMagie(self, pointsDeDegatsSort, autrePersonnage):
        self.estMort()
        if self.comparaison(autrePersonnage):
            luimeme = (f"{self.nom} c'est lui-même !")
            print(luimeme)
            return luimeme

        elif not self.mort and not autrePersonnage.mort:
            if (pointsDeDegatsSort) > (autrePersonnage).vie:
                autrePersonnage.vie += pointsDeDegatsSort
                soigne = (f"{autrePersonnage.nom} a été soigné, il gagne {pointsDeDegatsSort} points de vie\n{autrePersonnage.nom} a {autrePersonnage.vie} points de vie")
                print (soigne)
                return soigne
            
            elif abs(self.pointsDeMagie) >= abs(pointsDeDegatsSort):
                self.pointsDeMagie -= abs(pointsDeDegatsSort)
                autrePersonnage.vie -= pointsDeDegatsSort
                resultat = (f"Il reste à {self.nom} "
                            f"{self.pointsDeMagie} points de magie\n"
                            f"{autrePersonnage.nom} a subit une attaque\n"
                            f"il perd {pointsDeDegatsSort} points de vie\n"
                            f"{autrePersonnage.nom} a "
                            f"{autrePersonnage.vie} points de vie")
                print(resultat)
                return resultat
            

            else:
                pasassez = (f"{self.nom} n'a pas assez "
                            "de points de magie pour affliger ce sort")
                print(pasassez)

race_humaine = Race("Humain", "Français")
race_extraterrestre = Race("Extraterrestre", "Ruine")