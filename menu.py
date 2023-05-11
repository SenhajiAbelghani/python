import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import ImageTk, Image

def admi_page():
    # Vérifier l'authentification de l'administrateur
    if authenticate_admin():
        menu.destroy()
        import admi
    else:
        messagebox.showerror("Accès refusé", "Vous n'êtes pas l'administrateur")

def client_page():
    # Mettez ici le code pour la page client
    messagebox.showinfo("Client", "Page client")

def authenticate_admin():
    # Demander à l'utilisateur de saisir un nom d'utilisateur et un mot de passe
    username = simpledialog.askstring("Authentification", "Nom d'utilisateur :", parent=menu)
    password = simpledialog.askstring("Authentification", "Mot de passe :", parent=menu, show="*")

    # Vérifier les informations d'identification
    if username == "abderrafie" and password == "1234":
        return True
    else:
        return False

menu = tk.Tk()
menu.title('Admin/Client Page')
menu.geometry("900x600")
menu.resizable(False, False)

title_label = tk.Label(menu, text="Welcome to El Fakir Location", font=("Elephant", 15), bg="firebrick1", fg="white")
title_label.place(x=0, y=0, relwidth=1, height=50)

# Fonction pour centrer les boutons
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Frame pour les boutons
button_frame = tk.Frame(menu)
button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Image client
client_image = Image.open("client.png")
client_image = client_image.resize((200, 200), Image.ANTIALIAS)
client_photo = ImageTk.PhotoImage(client_image)

client_label = tk.Label(button_frame, image=client_photo)
client_label.pack(side=tk.LEFT, padx=10)

# Bouton Client
client_button = tk.Button(button_frame, text="Client", width=10, height=3, command=client_page)
client_button.pack(side=tk.LEFT, pady=10)

# Image admin
admin_image = Image.open("admin.png")
admin_image = admin_image.resize((200, 200), Image.ANTIALIAS)
admin_photo = ImageTk.PhotoImage(admin_image)

admin_label = tk.Label(button_frame, image=admin_photo)
admin_label.pack(side=tk.RIGHT, padx=10)
# Bouton Admin
admin_button = tk.Button(button_frame, text="Admin", width=10, height=3, command=admi_page)
admin_button.pack(side=tk.RIGHT, pady=10)

# Centrer la fenêtre
center_window(menu)

# Lancement de la boucle principale
menu.mainloop()
