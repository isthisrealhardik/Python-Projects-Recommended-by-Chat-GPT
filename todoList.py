# Todo List App
# App would allow you to add and delete tasks

# Import tkinter gui for operations on tasks visually.
import tkinter as tk

# initiate a window
root = tk.Tk()
root.title("To Do List App")

# create a function to add tasks
def addOnClick():
    value = inputEntry.get()
    listBox.insert(tk.END, value)
    inputEntry.delete(0, tk.END)

# create a function to delete tasks
def delOnClick():
    selected = listBox.curselection()
    listBox.delete(selected)


# Set up the widgets

# --- Label for 'adding a todo'
labelAdd = tk.Label(root, text='Add a todo?')
# --- Input for 'adding a todo'
inputEntry = tk.Entry(root)
# --- Button for 'adding a todo'
buttonAdd = tk.Button(root, text='Add', command=addOnClick)
# --- Button for 'deleting a selected todo'
buttonDel = tk.Button(root, text='Del', command=delOnClick)
# --- Listbox for 'adding a todo'
listBox = tk.Listbox(root)


# packing widgets
labelAdd.pack()
inputEntry.pack()
buttonAdd.pack()
buttonDel.pack()
listBox.pack()

# finish the mainloop
root.mainloop()
