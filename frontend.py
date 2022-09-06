# This is the Frontend interface for this music store app.

from tkinter import *
import backend


def get_selected_row(event):
    try:
        global selected_row
        idx = listbox.curselection()[0]
        selected_row = listbox.get(idx)
        entry_one.delete(0, END)
        entry_one.insert(END, selected_row[1])
        entry_two.delete(0, END)
        entry_two.insert(END, selected_row[2])
        entry_three.delete(0, END)
        entry_three.insert(END, selected_row[3])
        entry_four.delete(0, END)
        entry_four.insert(END, selected_row[4])
        entry_five.delete(0, END)
        entry_five.insert(END, selected_row[5])

    except IndexError:
        pass


def show_command():
    listbox.delete(0, END)
    for row in backend.view():
        listbox.insert(END, row)


def search_command():
    listbox.delete(0, END)
    search_params = backend.search(title_text.get(), artiste_text.get(), genre_text.get(), year_text.get(),
                                   copyright_text.get())
    for row in search_params:
        listbox.insert(END, row)


def add_command():
    backend.insert(title_text.get(), artiste_text.get(), genre_text.get(), year_text.get(),
                   copyright_text.get())
    listbox.delete(0, END)
    listbox.insert(END, (title_text.get(), artiste_text.get(), genre_text.get(), year_text.get(),
                         copyright_text.get()))

    title_text.set("")
    artiste_text.set("")
    genre_text.set("")
    year_text.set("")
    copyright_text.set("")


def delete_command():
    backend.delete(selected_row[0])


def update_command():
    backend.update(selected_row[0], title_text.get(), artiste_text.get(), genre_text.get(), year_text.get(),
                   copyright_text.get())


def close_command():
    window.destroy()


window = Tk()
window.wm_title("Inventor Music Store")
# Grid Labels
title = Label(window, text="Title")
title.grid(row=0, column=0)

artiste = Label(window, text="Artiste")
artiste.grid(row=0, column=2)

genre = Label(window, text="Genre")
genre.grid(row=0, column=4)

year = Label(window, text="Year")
year.grid(row=1, column=0)

copyright = Label(window, text="Copyright")
copyright.grid(row=1, column=2)

# Entry Widgets
title_text = StringVar()
entry_one = Entry(window, textvariable=title_text)
entry_one.grid(row=0, column=1)

artiste_text = StringVar()
entry_two = Entry(window, textvariable=artiste_text)
entry_two.grid(row=0, column=3)

genre_text = StringVar()
entry_three = Entry(window, textvariable=genre_text)
entry_three.grid(row=0, column=5)

year_text = StringVar()
entry_four = Entry(window, textvariable=year_text)
entry_four.grid(row=1, column=1)

copyright_text = StringVar()
entry_five = Entry(window, textvariable=copyright_text)
entry_five.grid(row=1, column=3)

# Listbox
listbox = Listbox(window, height=6, width=35)
listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

# Scrollbar
scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)

# Config
listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

# Bind Widgets
listbox.bind("<<ListboxSelect>>", get_selected_row)

# Buttons
button1 = Button(window, text="Show list", width=14, command=show_command)
button1.grid(row=2, column=3)

button2 = Button(window, text="Search song", width=14, command=search_command)
button2.grid(row=3, column=3)

button3 = Button(window, text="Add song", width=14, command=add_command)
button3.grid(row=4, column=3)

button4 = Button(window, text="Update selected", width=14, command=update_command)
button4.grid(row=5, column=3)

button5 = Button(window, text="Delete selected", width=14, command=delete_command)
button5.grid(row=6, column=3)

button5 = Button(window, text="Close", width=14, command=close_command)
button5.grid(row=7, column=3)

window.mainloop()
