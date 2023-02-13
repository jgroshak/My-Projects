from tkinter import *
import back_end

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass
    


# Functions to connect back_end to front_end 
 # 1) Add wrapper function to button
 # 2) 

def view_command():
# to make sure the list is not duplicated each time the button is pressed
    list1.delete(0,END)
    for row in back_end.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in back_end.search(e1.get(),e2.get(),e3.get(),e4.get()):
        list1.insert(END,row)

def add_command():
    back_end.insert(e1.get(),e2.get(),e3.get(),e4.get())
    list1.delete(0,END)
    list1.insert(END,(e1.get(),e2.get(),e3.get(),e4.get()))


def delete_command():
    back_end.delete(selected_tuple[0])


def update_command():
    back_end.update(selected_tuple[0],e1.get(),e2.get(),e3.get(),e4.get())





window = Tk()
window.wm_title("Book Database")


# labels for text entry
l1 = Label(window, text="Title")
l1.grid(column=0, row=0)

l2 = Label(window, text="Author")
l2.grid(column=0, row=1)

l3 = Label(window, text="Year")
l3.grid(column=2, row=0)

l4 = Label(window, text="ISBN")
l4.grid(column=2, row=1)

# spatial data types for entries
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(column=1, row=0)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(column=1, row=1)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(column=3, row=0)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(column=3, row=1)

# Listbox for displaying results
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# Scrollbar 
scroll_bar = Scrollbar(window)
scroll_bar.grid(row=2,column=2, rowspan=6)

list1.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list1.yview)


# Needed for delete_command function
list1.bind('<<ListboxSelect>>',get_selected_row)

# Widget buttons for 'view all', 'search entry', 'add entry', 'update', 'delete', 'close' 
b1 = Button(window, text="View All", width=12, command=view_command)
#                                                           ^ we dont add () to the function beacuse we want it executed when the button is pressed (not when the script is run)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)


window.mainloop()


