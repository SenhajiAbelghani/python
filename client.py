import tkinter as tk
from tkinter import ttk

class CarRental:
    def init(self, root):
        self.root = root
        self.root.title("Location de voitures")
        self.create_widgets()

    def create_widgets(self):
        # Labels pour les informations de location
        tk.Label(self.root, text="Matricule de voiture:").grid(row=0, column=0)
        self.matricule_ent = tk.Entry(self.root)
        self.matricule_ent.grid(row=0, column=1)

        tk.Label(self.root, text="Nom de client:").grid(row=1, column=0)
        self.client_nom_ent = tk.Entry(self.root)
        self.client_nom_ent.grid(row=1, column=1)

        tk.Label(self.root, text="Contact de client:").grid(row=2, column=0)
        self.client_contact_ent = tk.Entry(self.root)
        self.client_contact_ent.grid(row=2, column=1)

        tk.Label(self.root, text="Durée de location:").grid(row=3, column=0)
        self.duree_ent = tk.Entry(self.root)
        self.duree_ent.grid(row=3, column=1)

        tk.Label(self.root, text="Contact de chauffeur:").grid(row=4, column=0)
        self.chauffeur_contact_ent = tk.Entry(self.root)
        self.chauffeur_contact_ent.grid(row=4, column=1)

        # Boutons pour les actions
        tk.Button(self.root, text="Enregistrer", command=self.enregistrer).grid(row=5, column=0)
        tk.Button(self.root, text="Modifier", command=self.modifier).grid(row=5, column=1)
        tk.Button(self.root, text="Annuler", command=self.annuler).grid(row=5, column=2)
        tk.Button(self.root, text="Valider", command=self.valider).grid(row=5, column=3)

        # Tableau pour afficher les voitures disponibles
        self.voitures_tab = ttk.Treeview(self.root, columns=("matricule", "nom", "prix"))
        self.voitures_tab.heading("matricule", text="Numéro de matricule")
        self.voitures_tab.heading("nom", text="Nom de voiture")
        self.voitures_tab.heading("prix", text="Prix de location")
        self.voitures_tab.grid(row=6, column=0, columnspan=4)

        # Tableau pour afficher les locations en cours
        self.locations_tab = ttk.Treeview(self.root, columns=("matricule", "nom_client", "date_debut", "date_fin"))
        self.locations_tab.heading("matricule", text="Numéro de matricule")
        self.locations_tab.heading("nom_client", text="Nom de client")
        self.locations_tab.heading("date_debut", text="Date de début")
        self.locations_tab.heading("date_fin", text="Date de fin")
        self.locations_tab.grid(row=7, column=0, columnspan=4)

        # Exemple de données pour le tableau des voitures disponibles
        self.voitures_tab.insert("", "end", text="1", values=("AB-1234", "Renault Clio", "300dh/jour"))
        self.voitures_tab.insert("", "end", text="2", values=("CD-5678", "Peugeot 308", "450dh/jour"))
        self.voitures_tab.insert("", "end", text="3", values=("EF-9012", "siat leon", "250dh€/jour"))
        self.voitures_tab.insert("", "end", text="4", values=("GH-3456", " Golf7", "350dh/jour"))

        # Exemple de données pour le tableau des locations en cours
        self.locations_tab.insert("", "end", text="1", values=("AB-1234", "Senhaji Abdelghani", "2023-05-10", "2023-05-12"))
        self.locations_tab.insert("", "end", text="2", values=("CD-5678", "ELfakir Abderrafie", "2023-05-11", "2023-05-14"))
        self.locations_tab.insert("", "end", text="3", values=("EF-9012", "Briki Mohammed amine", "2023-05-15", "2023-05-19"))

    def enregistrer(self):
        # TODO: Ajouter le code pour enregistrer les informations de location dans une base de données
        print("Enregistrer")

    def modifier(self):
        # TODO: Ajouter le code pour modifier les informations de location dans une base de données
        print("Modifier")

    def annuler(self):
        # TODO: Ajouter le code pour annuler les informations de location saisies
        print("Annuler")

    def valider(self):
        # TODO: Ajouter le code pour valider les informations de location saisies
        print("Valider")

if NamedFuncPointer == "_main":
    root = tk.Tk()
    app = CarRental(root)
    root.mainloop()