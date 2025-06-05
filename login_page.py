from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error',"All fields are required")
    elif usernameEntry.get()=='Kalyani' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Login Successfully')
        window.destroy()
        import ems
    else:
        messagebox.showerror('Error','Invalid Credentials')
        
window=CTk()
window.geometry('930x478+100+100')
window.resizable(0,0)
window.title('Login Page')

image=CTkImage(Image.open("A:\Employement_database_project\login_page_pic.png"),size=(600,270))
imageLabel=CTkLabel(window,image=image,text='')
imageLabel.place(x=320,y=110)

headinglabel=CTkLabel(window,text='Employee Management System',bg_color='#FAFAFA',font=('Goudy Old Style',20,'bold'),text_color='dark blue')
headinglabel.place(x=20,y=100)

usernameEntry=CTkEntry(window,placeholder_text='Enter Your Username',width=180)
usernameEntry.place(x=50,y=150)

passwordEntry=CTkEntry(window,placeholder_text='Enter Your Password',width=180,show="*")
passwordEntry.place(x=50,y=200)

loginButton=CTkButton(window,text='Login',cursor='hand2',command=login)
loginButton.place(x=65,y=250)

window.mainloop()