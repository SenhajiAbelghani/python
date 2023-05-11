from tkinter import *
def menu_page():
    fenetre.destroy()
    import menu
# Fonction pour gérer le clic sur le bouton "ADD NEW CAR"
def ajouter_voiture():
    # Code pour ajouter une nouvelle voiture ici
    print("Ajouter une nouvelle voiture")

# Fonction pour gérer le clic sur le bouton "DELETE A CAR"
def supprimer_voiture():
    # Code pour supprimer une voiture ici
    print("Supprimer une voiture")

# Fonction pour gérer le clic sur le bouton "REMPLIR CONTRAT"
def remplir_contrat():
    # Code pour remplir un contrat ici
    print("Remplir un contrat")

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Gestion de location de voitures")

# Création des boutons
btn_ajouter_voiture = Button(fenetre, text="ADD NEW CAR", command=ajouter_voiture)
btn_ajouter_voiture.pack(pady=10)

btn_supprimer_voiture = Button(fenetre, text="DELETE A CAR", command=supprimer_voiture)
btn_supprimer_voiture.pack(pady=10)

btn_remplir_contrat = Button(fenetre, text="REMPLIR CONTRAT", command=remplir_contrat)
btn_remplir_contrat.pack(pady=10)

# Lancement de la boucle principale
fenetre.mainloop()
