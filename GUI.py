from merge import *

from tkinter import *
from tkinter import ttk

# Define the function to call when ButtonOk is clicked...
def btnOk1_clicked():
    x = int(entry1.get())
    y = int(entry2.get())
    mergePDF(x,y)
    
def btnOk2_clicked():
    x = entry3.get()
    y = entry4.get()
    mergingRandomName(x, y)
    

def btnCancel_clicked():
    window.destroy()  

# Create the Window and give it a title...
window = Tk()
window.title("PDFJOINER")

# Set the Windows size...
window.geometry('900x600')

# Scale it up so we can see it better...
window.tk.call('tk', 'scaling', 3.0)

#############
#   Widgets #
#############

# Create our label...
lbl = Label(window, text="Here you can Concatenate two PDFs by Number")
lbl.grid(column=0, row=0)

# Create our label...
lbl = Label(window, text="Enter a Start number: ")
lbl.grid(column=0, row=1)

# Create the entry box
entry1 = Entry(window, textvariable="Start")
entry1.grid(column=1, row=1)

# Create our label...
lbl = Label(window, text="Enter a end number: ")
lbl.grid(column=0, row=2)

# Create the entry box
entry2 = Entry(window, textvariable="End")
entry2.grid(column=1, row=2)

btnOk = Button(window, text="Ok", command=btnOk1_clicked)
btnOk.grid(column=0, row=3)

# Create our label...
lbl = Label(window, text="Here you can Concatenate two PDFs by Name")
lbl.grid(column=0, row=4)

# Create our label...
lbl = Label(window, text="Enter first Name: ")
lbl.grid(column=0, row=5)

# Create the entry box
entry3 = Entry(window, textvariable="First")
entry3.grid(column=1, row=5)

# Create our label...
lbl = Label(window, text="Enter second Name: ")
lbl.grid(column=0, row=6)

# Create the entry box
entry4 = Entry(window, textvariable="Second")
entry4.grid(column=1, row=6)

btnOk2 = Button(window, text="Ok", command=btnOk2_clicked)
btnOk2.grid(column=0, row=7)

btnCancel = Button(window, text="Cancel", command=btnCancel_clicked)
btnCancel.grid(row=8)

window.mainloop()
