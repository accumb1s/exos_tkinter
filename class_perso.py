class Personnage:
    def __init__(self,vie,nom,force,endurance,rapidite,intelligence, img_path):
            self.vie = vie
            self.nom = nom
            self.force = force
            self.endurance = endurance
            self.rapidite = rapidite
            self.intelligence = intelligence
            self.esquive = False
            self.PointsDeDeplacement = 0
            self.img_path = img_path
            self.estMort()

    def estMort(self):
        if self.vie > 0:
            self.mort = False
        else :
            self.mort = True

    def afficheEtat(self):
        self.estMort()
        if self.mort:
            estmort = (f"{self.nom} est mort")
            print (estmort)
            return estmort.rstrip()
        else :
            self.restevie = (f"Il reste {self.vie} points de vie à {self.nom}")
            print (self.restevie)
            return self.restevie

    def afficheCaracteristiques(self):
        caract = (f"{self.nom} a une force de {self.force},\nune endurance de {self.endurance}\nune rapidite de {self.rapidite}\net une intelligence de {self.intelligence}")
        print (caract)
        return caract
    
    def perdVie(self, nbPointsDeViePerdus):
        self.estMort()
        if self.mort:
            self.estmort = (f"Looser, {self.nom} as subit une attaque mortelle")
            print (self.estmort)
            return self.estmort
        else:
            # self.nbPointsDeViePerdus = nbPointsDeViePerdus
            self.vie -= nbPointsDeViePerdus
            self.perdvie = (f"{self.nom} a subit une attaque, il perd {nbPointsDeViePerdus} points de vie")
            print (self.perdvie)
            return self.perdvie
            # self.estMort()

    def gagneVie(self,nbPointVieGagne):
        self.estMort()
        if self.mort:
            self.estmort = (f"{self.nom} ne peut pas être soigné car il est mort !")
            print(self.estmort)
            return self.estmort
        else:
            self.vie += nbPointVieGagne
            self.soignevie = (f"{self.nom} a été soigné. Ses points de vies valent maintenant {self.vie}")
            print(self.soignevie)
            return self.soignevie

    def esquiveAttaque(self,autrePersonnage):
        rapidCalcul = int(self.rapidite * 1.2)
 
        if self.comparaison(autrePersonnage):
            self.comp = (f"{self.nom} ne peux pas esquiver {autrePersonnage.nom}. c'est lui-même !")
            print (self.comp)
            return self.comp
        elif rapidCalcul > autrePersonnage.force and not self.mort and not autrePersonnage.mort:
            # self.esquive = True
            self.calcul = (f"{self.nom} esquive l'attaque de {autrePersonnage.nom}\nEsquive : calcul de rapidité de {self.nom} : {self.rapidite} contre\n{autrePersonnage.rapidite} pour la force de {autrePersonnage.nom}")
            print (self.calcul)
            return self.calcul
        elif self.mort:
            self.estmort = (f"{self.nom} ne peut esquiver l'attaque de {autrePersonnage.nom} : {self.nom} est mort")
            print (self.estmort)
            return self.estmort
        elif autrePersonnage.mort:
            self.autrepersomort = (f"{self.nom} ne peut esquiver l'attaque de {autrePersonnage.nom} : {autrePersonnage.nom} est mort")
            print (self.autrepersomort)
            return self.autrepersomort
        # else : print (f"{self.nom} et {autrePersonnage.nom} sont morts")

    def attaque(self,autrePersonnage):
        self.estMort()
        autrePersonnage.esquiveAttaque(self)
        if self.comparaison(autrePersonnage):
            self.comp = (f"{self.nom} ne peux pas attaquer {autrePersonnage.nom}. c'est lui-même !")
            print (self.comp)
            return self.comp
        elif  not self.mort and not autrePersonnage.esquive:
            pointDeDegats = int(self.force * 0.6)
            autrePersonnage.perdVie(pointDeDegats)
            # autrePersonnage.vie -= pointDeDegats
        else :
            self.estmort = (f"{self.nom} ne peut attaquer personne : Il est mort !")
            print(self.estmort)
            return self.estmort
            # if not autrePersonnage.mort:
            #     print (f"{self.nom} attaque {autrePersonnage.nom} de {pointDeDegats} point de degats, il reste {autrePersonnage.vie} points de vie à {autrePersonnage.nom}")
            # else:
            #     print (f"{autrePersonnage.nom} est déjà mort !")

    def soigne(self,pointsDeSoin,autrePersonnage):
        
        self.estMort()
        if self.comparaison(autrePersonnage):
            self.comp = (f"{self.nom} ne peux pas soigner {autrePersonnage.nom}. c'est lui-même !")
            print (self.comp)
            return self.comp
        elif not self.mort and not autrePersonnage.mort:
            autrePersonnage.gagneVie(pointsDeSoin)
            self.restaur = (f"{self.nom} soigne {autrePersonnage.nom}. {self.nom} le restaure à {pointsDeSoin} point de vie")
            print (self.restaur)
            return self.restaur
        elif autrePersonnage.mort:
            self.estmort = (f"{self.nom} ne peux pas soigner {autrePersonnage.nom}. {autrePersonnage.nom} est mort !!")
            print (self.estmort)
            return self.estmort
        else:
            self.estmort = (f"{autrePersonnage.nom} ne peux pas être soigné par {self.nom}. {self.nom} est mort !!")
            print (self.estmort)
            return self.estmort
    
    def seDeplace(self,PointsDeDeplacement,autrePersonnage):
        self.estMort()
        if self.mort:
            self.estmort = (f"{self.nom} ne peut plus se déplacer car il est mort !")
            print (self.estmort)
            return self.estmort
        else:
            self.PointsDeDeplacement += PointsDeDeplacement
            if autrePersonnage.PointsDeDeplacement > 0:
                autrePersonnage.PointsDeDeplacement -= PointsDeDeplacement
                self.sedeplace = (f"{self.nom} se déplace de {self.PointsDeDeplacement} points\n"
                                f"{autrePersonnage.nom} se rapproche de {self.nom}\n"
                                 f"de {autrePersonnage.PointsDeDeplacement} points")
                print (self.sedeplace)
                return self.sedeplace
            else :
                self.sedeplace = (f"{self.nom} se déplace de {self.PointsDeDeplacement} points\n"
                                f"{autrePersonnage.nom} se rapproche de {self.nom}\n"
                                 f"de {autrePersonnage.PointsDeDeplacement} points")
                print (self.sedeplace)
                return self.sedeplace
    
    def comparaison(self,autrePersonnage):
        if self is autrePersonnage:
            return True
        else:
            return False
