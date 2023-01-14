from tkinter import *

window = Tk(className=" Book Database")


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
e2.grid(column=3, row=0)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(column=1, row=1)

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

# Widget buttons for 'view all', 'search entry', 'add entry', 'update', 'delete', 'close' 
b1 = Button(window, text="View All", width=12)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12)
b6.grid(row=7, column=3)


window.mainloop()


