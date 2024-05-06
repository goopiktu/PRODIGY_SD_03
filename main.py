from tkinter import *
import pandas as pd

data = pd.read_csv("./data.csv")

df = pd.DataFrame(data)

name = df['Name'].values
phone = df['Phone Number'].values
email = df['Email'].values

window = Tk() 
window.geometry("550x400") 
window.title("Contact Manager")

main_frame = Frame(window)
main_frame.grid(row=0, column=0, sticky="nsew")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

canvas = Canvas(main_frame, width=525, height=350)
canvas.grid(row=0, column=0, sticky="nsew")

scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.grid(row=0, column=6, sticky='ns')

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion= canvas.bbox("all")))

second_frame = Frame(canvas)

canvas.create_window((0,0), window=second_frame, anchor="nw")

def formLabels(form):
    nameTag = Label(form, text="Name")
    nameTag.grid(row=0, column=0)
    nameEntry = Entry(form, bd=5)
    nameEntry.grid(row=0, column=1)
    
    phoneTag = Label(form, text="Phone Number")
    phoneTag.grid(row=2, column=0)
    phoneEntry = Entry(form, bd=5)
    phoneEntry.grid(row=2, column=1)

    emailTag = Label(form, text="Email Address")
    emailTag.grid(row=4, column=0)
    emailEntry = Entry(form, bd=5)
    emailEntry.grid(row=4, column=1)

    return nameEntry, phoneEntry, emailEntry

def addForm():
    form = Toplevel()
    form.title("Add Form")
    form.geometry("240x150")

    nameEntry, phoneEntry, emailEntry = formLabels(form)

    submitButton = Button(form, text="Submit", command=lambda: addMethod(nameEntry.get() ,phoneEntry.get(), emailEntry.get(), form))
    submitButton.place(rely=1.0, relx=1.0, x=-5, y=-5, anchor=SE)

    form.focus()
    form.grab_set()

def editForm(i):
    form = Toplevel()
    form.title("Edit Form")
    form.geometry("240x150")

    colAsArray = df.iloc[i,:].values

    print(i)
    nameEntry, phoneEntry, emailEntry = formLabels(form)

    nameEntry.insert(END, colAsArray[0])
    phoneEntry.insert(END, colAsArray[1])
    emailEntry.insert(END, colAsArray[2])

    submitButton = Button(form, text="Submit", command=lambda: editMethod(nameEntry.get() ,phoneEntry.get(), emailEntry.get(), form, i))
    submitButton.place(rely=1.0, relx=1.0, x=-5, y=-5, anchor=SE)

    form.focus()
    form.grab_set()

  


def deleteMethod(index):
    print(df)
    df.drop(index, inplace=True)
    df.reset_index(inplace=True, drop=True)
    df.to_csv("./data.csv", index=False)
    print(df)
    refreshTable()
    populateTable()
    

def addMethod(nameEntry, phoneEntry, emailEntry, form):
    print(df)
    df.loc[len(df.index)] = [nameEntry, phoneEntry, emailEntry]
    df.to_csv("./data.csv", index=False)
    populateTable()
    print(df)
    form.destroy()

def editMethod(nameEntry, phoneEntry, emailEntry, form, i):
    print(df)
    df.loc[[i]] = [nameEntry, phoneEntry, emailEntry]
    df.to_csv("./data.csv", index=False)
    populateTable()
    print(df)
    form.destroy()
    print(df)
    
# Create lists
name_widgets = []
phone_widgets = []
email_widgets = []
delete_buttons = []
edit_buttons = []

# Populate table with data
def colLabels():
    name_label = Label(second_frame, text="Name")
    name_label.grid(row=0, column=0)
    phoneNumber_label = Label(second_frame, text="Phone Number")
    phoneNumber_label.grid(row=0, column=1)
    emailAddress_label = Label(second_frame, text="Email Address")
    emailAddress_label.grid(row=0, column=2)

def populateTable():

    colLabels()
    data = pd.read_csv("./data.csv")
    df = pd.DataFrame(data)

    name = df['Name'].values
    phone = df['Phone Number'].values
    email = df['Email'].values
    addButton = Button(text="Add", bd="5", command=lambda: addForm())
  
    addButton.place(rely=1.0, relx=1.0, x=-5, y=-5, anchor=SE)

    for i in range(len(name)):
        name_text = Label(second_frame, width=15, height=2, text=name[i], borderwidth=4, relief="ridge")
        name_text.grid(row=i+1, column=0)
    
        phone_text = Label(second_frame, width=15, height=2, text=phone[i], borderwidth=4, relief="ridge")
        phone_text.grid(row=i+1, column=1)
       
        email_text = Label(second_frame, width=25, height=2, text=email[i], borderwidth=4, relief="ridge")
        email_text.grid(row=i+1, column=2)
       
        delete_button = Button(second_frame, text="Delete", bd="5", command=lambda i=i: deleteMethod(i))
        delete_button.grid(row=i+1, column=3)
        
        edit_button = Button(second_frame, text="Edit", bd="5", command=lambda i=i: editForm(i))
        edit_button.grid(row=i+1, column=4)

   
    
        


def refreshTable():
    for widget in second_frame.winfo_children():
        widget.destroy()
    populateTable()

populateTable()
window.mainloop()
