from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import database

def delete_all():
    result=messagebox.askyesno('Confirm','Do you really want to delete all the records?')
    if result:
        database.delete_all()
        treeview_data()
        
    
def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set('Search By')
    clear()

def search_employee():
    if searchEntry.get()=='':
        messagebox.showerror('Error','Enter Value to Search')
    elif searchBox.get()=='Search By':
        messagebox.showerror('Error','Select any option to Search')
    else:
        searched_data=database.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for i in searched_data:
            tree.insert('',END,values=i) 

def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to delete')
    else:
        database.delete_employee(idEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Deleted Successfully')

def update_employee():
    selected_id=tree.selection()
    if not selected_id:
        messagebox.showerror('Error','Select data to Update')
    else:
        database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())    
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data Updated Sucessfully')

def selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0,row[5])
    
    

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    roleBox.set('Web Developer')
    genderBox.set('Female')
    salaryEntry.delete(0,END)

def treeview_data():
    employees=database.fetch_employees()
    tree.delete(*tree.get_children())
    for i in employees:
        tree.insert('',END,values=i)
    
    
def add_employee():
    if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or salaryEntry.get()=='':
        messagebox.showerror('Error','All Fields are Required')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error','Id Already Exists')
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror("Error","Invalid ID format. Use 'EMP' followed by a number (e.g., 'EMP1').")
    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data Added Successfully')
    
window1=CTk()
window1.geometry('930x580+100+100')
window1.resizable(0,0)
window1.title('Employee Management System')
window1.configure(fg_color='#161C30')

image=CTkImage(Image.open("A:\Employement_database_project\ems_top_image.jpg"),size=(930,158))
logoLabel=CTkLabel(window1,image=image,text="")
logoLabel.grid(row=0,column=0,columnspan=2)

leftFrame=CTkFrame(window1,fg_color='#161C30')
leftFrame.place(x=0,y=180)


idLabel=CTkLabel(leftFrame,text='Id',font=("Arial",18,'bold'),text_color='white')
idLabel.grid(row=0,column=0,padx=10,pady=10,sticky='w')

idEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
idEntry.grid(row=0,column=1)

nameLabel=CTkLabel(leftFrame,text='Name',font=('arial',18,'bold'),text_color='white')
nameLabel.grid(row=1,column=0,padx=10,pady=10,sticky='w')

nameEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
nameEntry.grid(row=1,column=1)

phoneLabel=CTkLabel(leftFrame,text='Phone',font=('arial',18,'bold'),text_color='white')
phoneLabel.grid(row=3,column=0,padx=10,pady=10,sticky='w')

phoneEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
phoneEntry.grid(row=3,column=1)

roleLabel=CTkLabel(leftFrame,text='Role',font=('arial',18,'bold'),text_color='white')
roleLabel.grid(row=4,column=0,padx=10,pady=10,sticky='w')

role_options=['Web Developer','Cloud Architect','Technical Writer','Network Engineer','Devops Engineer','Data Scientist','Business Analyst','IT Consultant','UX/UI Designer']
roleBox=CTkComboBox(leftFrame,values=role_options,font=('arial',15,'bold'),width=180,state='readonly')
roleBox.grid(row=4,column=1)
roleBox.set(role_options[0])

genderLabel=CTkLabel(leftFrame,text="Gender",font=('Arial',18,'bold'),text_color='white')
genderLabel.grid(row=5,column=0,padx=10,pady=10,sticky='w')

genderBox=CTkComboBox(leftFrame,values=['Male','Female'],font=('arial',15,'bold'),width=180,state='readonly')
genderBox.grid(row=5,column=1)
genderBox.set('Female')

salaryLabel=CTkLabel(leftFrame,text='Salary',font=('arial',18,'bold'),text_color='white')
salaryLabel.grid(row=6,column=0,padx=10,pady=10,sticky='w')


salaryEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
salaryEntry.grid(row=6,column=1)

rightFrame=CTkFrame(window1)
rightFrame.place(x=280,y=180)

search_options=['Id','Name','Phone','Role',"Gender",'Salary']
searchBox=CTkComboBox(rightFrame,values=search_options,state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('Search By')

searchEntry=CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightFrame,text='Search',width=100,command=search_employee)
searchButton.grid(row=0,column=2)

showAllButton=CTkButton(rightFrame,text='Show All',width=100,command=show_all)
showAllButton.grid(row=0,column=3,pady=5)

tree=ttk.Treeview(rightFrame,height=11)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=('Id','Name','Phone','Role',"Gender",'Salary')
tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')
tree.config(show='headings')
tree.column('Id',anchor=CENTER,width=50)
tree.column('Name',anchor=CENTER,width=110)
tree.column('Phone',anchor=CENTER,width=130)
tree.column('Role',anchor=CENTER,width=150)
tree.column('Gender',anchor=CENTER,width=90)
tree.column('Salary',anchor=CENTER,width=100)

style=ttk.Style()
style.configure('Treeview.Heading',font=('arial',13,'bold'))
style.configure("Treeview",font=('arial',10,'bold'),background='#161C30',foreground='white')

scrollbar=ttk.Scrollbar(rightFrame,orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')

tree.config(yscrollcommand=scrollbar.set)

buttonFrame=CTkFrame(window1,fg_color='#161C30')
buttonFrame.place(x=40,y=510)

newButton=CTkButton(buttonFrame,text='New Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=lambda:clear(True))
newButton.grid(row=0,column=0,pady=5)

addButton=CTkButton(buttonFrame,text='Add Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=1,pady=5,padx=5)


updateButton=CTkButton(buttonFrame,text='Update Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=update_employee)
updateButton.grid(row=0,column=2,pady=5,padx=5)

deleteButton=CTkButton(buttonFrame,text='Delete Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_employee)
deleteButton.grid(row=0,column=3,pady=5,padx=5)

deleteallButton=CTkButton(buttonFrame,text='Delete All',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_all)
deleteallButton.grid(row=0,column=4,pady=5,padx=5)

treeview_data()
window1.bind('<ButtonRelease>',selection)
window1.mainloop()