import tkinter as tk

def menu_page():
    root.destroy()
    import menu

# Fonction pour gérer le clic sur le bouton "ADD NEW CAR"
def ajouter_voiture():
    # Code pour ajouter une nouvelle voiture ici
    print("Ajouter une nouvelle voiture")
    root.destroy()
    import ajouter_voiture
# Fonction pour gérer le clic sur le bouton "DELETE A CAR"
def supprimer_voiture():
    # Code pour supprimer une voiture ici
    print("Supprimer une voiture")

# Fonction pour gérer le clic sur le bouton "REMPLIR CONTRAT"
def remplir_contrat():
    # Code pour remplir un contrat ici
    print("Remplir un contrat")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Admin Page")
root.geometry("400x300")


# Création des boutons avec des options de style
button_style = {"font": ("Arial", 12), "fg": "black", "bg": "firebrick1", "width": 15, "height": 2}

btn_ajouter_voiture = tk.Button(root, text="ADD NEW CAR", command=ajouter_voiture, **button_style)
btn_ajouter_voiture.pack(pady=10)

btn_supprimer_voiture = tk.Button(root, text="DELETE A CAR", command=supprimer_voiture, **button_style)
btn_supprimer_voiture.pack(pady=10)

btn_remplir_contrat = tk.Button(root, text="REMPLIR CONTRAT", command=remplir_contrat, **button_style)
btn_remplir_contrat.pack(pady=10)

# Lancement de la boucle principale
root.mainloop()
