from tkinter import *
from PIL import ImageTk

def menu_page():
    login_window.destroy()
    import menu


# Functionality Part
def signup_page():
    login_window.destroy()
    import signup
def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)
def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)
def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)
# GUI PART
login_window = Tk()
login_window.geometry('916x662+50+50')
login_window.resizable(0, 0)
login_window.title('Login Page')

bgImage = ImageTk.PhotoImage(file='bg.jpg')
bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(login_window, text='USER LOGIN', font=('Microsoft YaHei UI Light', 23, 'bold'), bg='white', fg='firebrick1')
heading.place(x=540, y=120)

usernameEntry = Entry(login_window, width=25, font=('Microsoft YaHei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
usernameEntry.place(x=508, y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)

frame1=Frame(login_window, width=250, height=2, bg='firebrick1')
frame1.place(x=508, y=222)


passwordEntry = Entry(login_window, width=25, font=('Microsoft YaHei UI Light', 11, 'bold'), bd=0, fg='firebrick1')
passwordEntry.place(x=508, y=260)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)

frame2=Frame(login_window, width=250, height=2, bg='firebrick1')
frame2.place(x=508, y=282)


openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window, image=openeye, bd=0,bg='white', activebackground='white', cursor='hand2',command=hide)
eyeButton.place(x=730, y=255)


forgetButton=Button(login_window, text='Forget Password?', bd=0,bg='white', activebackground='white', cursor='hand2', font=('Microsoft Yahei UI Light', 9, 'bold'), fg='firebrick1', activeforeground='firebrick1')
forgetButton.place(x=665, y=295)


loginButton=Button(login_window, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1',activeforeground='white', activebackground='firebrick1', cursor='hand2', bd=0, width=19,command=menu_page)
loginButton.place(x=508, y=350)


orLabel=Label(login_window, text='----------------OR----------------', font=('Open Sans', 16 ), fg='firebrick1',bg='white')
orLabel.place(x=505,y=400)


facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(login_window,image=facebook_logo, bg='white')
fbLabel.place(x=590, y=440)


google_logo=PhotoImage(file='google.png')
googleLabel=Label(login_window,image=google_logo, bg='white')
googleLabel.place(x=625, y=440)


twitter_logo=PhotoImage(file='twitter.png')
twitterLabel=Label(login_window,image=twitter_logo, bg='white')
twitterLabel.place(x=660, y=440)


signupLabel=Label(login_window, text='Dont have an account?', font=('Open Sans', 9,'bold'), fg='firebrick1',bg='white')
signupLabel.place(x=505,y=500)

newaccountButton=Button(login_window, text='Create New One', font=('Open Sans', 9, 'bold underline'), fg='blue', bg='white',activeforeground='white', activebackground='blue', cursor='hand2', bd=0, command=signup_page)
newaccountButton.place(x=657, y=500)
login_window.mainloop()
