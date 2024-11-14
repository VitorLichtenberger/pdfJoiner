from merge import *

from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tkinter.filedialog import askopenfilename

import glob
import os

# Define the function to call when ButtonOk is clicked...
def btnselect_clicked():
    pdf_list = select_all_pdfs()
    mergePDF(pdf_list)
    
def btnOk2_clicked():
    x = entry3.get()
    y = entry4.get()
    mergingRandomName(x, y)
    

def btnCancel_clicked():
    window.destroy()  

def open_file_dialog(ent):
    # Open file dialog and get the filename
    filename = askopenfilename()
    # Set the filename in entry4
    ent.delete(0, 'end')
    ent.insert(0, filename)
    
# Function to open a directory dialog and get all PDF files
def select_all_pdfs():
    # Open a dialog to select a folder
    folder_path = filedialog.askdirectory()
    list_of_PDF = []
    # Check if a folder was selected
    if folder_path:
        # Use glob to find all PDFs in the selected folder
        pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))
        
        # Display or process the PDF files
        if pdf_files:
            return pdf_files
            
        else:
            print("No PDF files found in the selected directory.")
    
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
lbl = Label(window, text="Here you can Concatenate all PDFs in a Folder")
lbl.grid(column=0, row=0)

# # Create our label...
# lbl = Label(window, text="Enter a start number:")
# lbl.grid(column=0, row=1)

# # Create the entry box
# entry1 = Entry(window, textvariable="Start")
# entry1.grid(column=1, row=1)

# # Create our label...
# lbl = Label(window, text="Enter a end number:")
# lbl.grid(column=0, row=2)

# # Create the entry box
# entry2 = Entry(window, textvariable="End")
# entry2.grid(column=1, row=2)



# Button to open the directory dialog and list PDFs
btn_select_pdfs = Button(window, text="Select PDFs", command=btnselect_clicked)
btn_select_pdfs.grid(column=1, row=0)


# Create our label...
lbl = Label(window, text="Here you can Concatenate two PDFs")
lbl.grid(column=0, row=4)

# Create our label...
lbl = Label(window, text="Select first: ")
lbl.grid(column=0, row=5)

entry3 = Entry(window)
entry3.grid(column=1, row=5)
# Bind the entry4 box to open the file dialog on click
entry3.bind("<Button-1>", lambda e: open_file_dialog(entry3))

# Create our label...
lbl = Label(window, text="Select second: ")
lbl.grid(column=0, row=6)

entry4 = Entry(window)
entry4.grid(column=1, row=6)
# Bind the entry4 box to open the file dialog on click
entry4.bind("<Button-1>", lambda e: open_file_dialog(entry4))

btnOk2 = Button(window, text="Ok", command=btnOk2_clicked)
btnOk2.grid(column=0, row=7)

btnCancel = Button(window, text="Cancel", command=btnCancel_clicked)
btnCancel.grid(row=8)

window.mainloop()
