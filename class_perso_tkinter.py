import tkinter as tk
from tkinter import *
import class_magicien as cm
from PIL import Image,ImageTk
# import customtkinter
import os

cwd = os.getcwd()
print (cwd)

class Combat:
    def __init__(self):
        self.Player_constructor()
        self.Win_constructor()
        self.affichage_text()
        self.Button_constructor()
    
    def Player_constructor(self):
        # self.joueur1 = cm.cp.Personnage(500, 'Franck', 20, 100, 100, 100, 'perso.png', 100, 150)
        # self.joueur2 = cm.cp.Personnage(500, 'David', 30, 100, 100, 100, 'perso.png', 400, 150)
        self.joueur1 = cm.Magicien(500, "Actarus", 500, 20, 20, 20, 500, cm.race_humaine,'actarus.jpg')
        self.joueur2 = cm.Magicien(500, "Hydargos", 500, 10, 10, 20, 500, cm.race_extraterrestre,'Hydargos.jpg')
    
    def Frame_constructor(self,text):
        self.frame = LabelFrame(text=text)

    
    def Win_constructor(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title(f"Combat entre {self.joueur1.nom} et {self.joueur2.nom}")
        self.root.rowconfigure(0, minsize=100)
        self.root.columnconfigure(0, minsize=450)

        # Open the image using PIL
        image1_pil = Image.open(self.joueur1.img_path)
        # Resize the image
        image1_resized = image1_pil.resize((200, 300))
        #pil_image_flip = image1_resized.transpose(Image.FLIP_LEFT_RIGHT)
        # Convert the image to PhotoImage format
        self.image1 = ImageTk.PhotoImage(image1_resized)

        # Repeat the process for image2
        image2_pil = Image.open(self.joueur2.img_path)
        image2_resized = image2_pil.resize((200, 300))
        self.image2 = ImageTk.PhotoImage(image2_resized)

        # Création d'un label pour afficher l'image dans la fenêtre
        self.image_label1 = tk.Label(image=self.image1)
        self.image_label2 = tk.Label(image=self.image2)

        # Placement du label dans la grille de la fenêtre
        self.image_label1.grid(row=0, column=0)
        self.image_label2.grid(row=0, column=1)


    def joueur1_attaque_joueur2(self):
        self.joueur1.attaque(self.joueur2)
        self.affichage_text()
    
    def joueur1_soigne_joueur2(self):
        self.joueur1.soigne(1,self.joueur2)
        self.affichage_text()
    
    def joueur2_attaque_joueur1(self):
        self.joueur2.attaque(self.joueur1)
        self.affichage_text()
    
    def joueur2_soigne_joueur1(self):
        self.joueur2.soigne(1,self.joueur1)
        self.affichage_text()
    
    def joueur1_faitMagie_joueur2(self):
        self.joueur1.faireMagie(22,self.joueur2)
        self.affichage_text()
    
    def joueur2_faitMagie_joueur1(self):
        self.joueur2.faireMagie(31,self.joueur1)
        self.affichage_text()

    def joueur1_sedeplace(self):
        self.joueur1.seDeplace(1,self.joueur2)
        self.affichage_text()
    
    def joueur2_sedeplace(self):
        self.joueur2.seDeplace(1,self.joueur1)
        self.affichage_text()
    
    def Button_constructor(self):
        self.button_attaque1 = tk.Button(self.root, justify='left',text="Attaquer", command=self.joueur1_attaque_joueur2)
        self.button_attaque1.grid(row=80, column=0)
        self.button_soins1 = tk.Button(self.root,justify='left', text="Soigner", command=self.joueur1_soigne_joueur2)
        self.button_soins1.grid(row=90, column=0)
        self.button_sedeplace1 = tk.Button(self.root,justify='left', text="Se déplace", command=self.joueur1_sedeplace)
        self.button_sedeplace1.grid(row=100, column=0)
        self.button_magie1 = tk.Button(self.root,justify='left', text="Magie", command=self.joueur1_faitMagie_joueur2)
        self.button_magie1.grid(row=110, column=0)
        
        self.button_attaque2 = tk.Button(self.root,justify='right', text="Attaquer", command=self.joueur2_attaque_joueur1)
        self.button_attaque2.grid(row=80, column=1)
        self.button_soins2 = tk.Button(self.root,justify='right', text="Soigner", command=self.joueur2_soigne_joueur1)
        self.button_soins2.grid(row=90, column=1)
        self.button_sedeplace2 = tk.Button(self.root,justify='right', text="Se déplace", command=self.joueur2_sedeplace)
        self.button_sedeplace2.grid(row=100, column=1)
        self.button_magie2 = tk.Button(self.root, justify='right',text="Magie", command=self.joueur2_faitMagie_joueur1)
        self.button_magie2.grid(row=110, column=1)

    def affichage_text(self):

        result_label1 = tk.Label(self.root, justify='left', text=self.joueur1.afficheCaracteristiquesMagicien())
        result_label1.grid(row=10,column=0)

        result_label3 = tk.Label(self.root, justify='left', text=self.joueur1.seDeplace(0,self.joueur2))
        result_label3.grid(row=30,column=0)

        result_label10 = tk.Label(self.root, justify='right', text=self.joueur2.afficheCaracteristiquesMagicien())
        result_label10.grid(row=10,column=1)

        result_label30 = tk.Label(self.root, justify='right', text=self.joueur2.seDeplace(0,self.joueur1))
        result_label30.grid(row=30,column=1)
              
        
        if "mort" in self.joueur1.afficheEtat():
            for widget in self.root.grid_slaves():
                widget.grid_forget()
            result_label2 = tk.Label(self.root, justify='left', fg='red',  text=self.joueur1.afficheEtat())
            result_label2.grid(row=20,column=0)
        else:
            result_label2 = tk.Label(self.root, justify='left', text=self.joueur1.afficheEtat())
            result_label2.grid(row=20,column=0)
                
        if "mort" in self.joueur2.afficheEtat():
            for widget in self.root.grid_slaves():
                widget.grid_forget()
            result_label20 = tk.Label(self.root, fg='red', justify='right', text=self.joueur2.afficheEtat())
            result_label20.grid(row=20,column=1)
            result_label2 = tk.Label(self.root, justify='left', text=self.joueur1.afficheEtat())
            result_label2.grid(row=20,column=0)
        else:
            result_label20 = tk.Label(self.root, justify='right', text=self.joueur2.afficheEtat())
            result_label20.grid(row=20,column=1)
                

test = Combat()
test.root.mainloop()

