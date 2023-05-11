from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    idEntry.delete(0, END)
    modelEntry.delete(0, END)
    prixEntry.delete(0, END)
    matriculeEntry.delete(0, END)
    check.set(0)


def connect_database():
    if idEntry.get() == '' or modelEntry.get() == '' or prixEntry.get() == '' or matriculeEntry.get() == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='1234', database='addcar')
            mycursor = con.cursor()
        except pymysql.Error:
            messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')
            return

        try:
            query = 'CREATE TABLE IF NOT EXISTS data(id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,  model VARCHAR(50), prix VARCHAR(100), matricule VARCHAR(20))'
            mycursor.execute(query)
        except pymysql.Error:
            messagebox.showerror('Error', 'Error executing database query')
        else:
            query = 'INSERT INTO data(model, prix, matricule) VALUES (%s, %s, %s)'
            mycursor.execute(query, (modelEntry.get(), prixEntry.get(), matriculeEntry.get()))
            con.commit()
            messagebox.showinfo('Success', 'Registration is successful')
            clear()
        finally:
            mycursor.close()
            con.close()





signup_window = Tk()
signup_window.title('ADD CAR')
signup_window.resizable(False, False)

background = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(signup_window, image=background)
bgLabel.grid()

frame = Frame(signup_window, bg='white')
frame.place(x=554, y=100)

heading = Label(frame, text='ADD A NEW CAR', font=('Microsoft YaHei UI Light', 18, 'bold'), bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)

idLabel = Label(frame, text='ID', font=('Microsoft YaHei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
idLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10,0))

idEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='firebrick1')
idEntry.grid(row=2, column=0, sticky='w', padx=25)

modelLabel = Label(frame, text='MODEL', font=('Microsoft YaHei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
modelLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10,0))

modelEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='firebrick1')
modelEntry.grid(row=4, column=0, sticky='w', padx=25)

prixLabel = Label(frame, text='PRICE', font=('Microsoft YaHei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
prixLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10,0))

prixEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='firebrick1')
prixEntry.grid(row=6, column=0, sticky='w', padx=25)

matriculeLabel = Label(frame, text='MATRICULE', font=('Microsoft YaHei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
matriculeLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10,0))

matriculeEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white', bg='firebrick1')
matriculeEntry.grid(row=8, column=0, sticky='w', padx=25)


addcarButton=Button(frame, text='Add Car',font=('Open Sans',16 ,'bold'), bd=0, bg='firebrick1', fg='white', activebackground='firebrick1', activeforeground='white', width=17, command=connect_database)
addcarButton.grid(row=10, column=0, padx=25)


signup_window.mainloop()

