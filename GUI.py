from merge import *

from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tkinter.filedialog import askopenfilename

import glob
import os

# Define the function to call when ButtonOk is clicked...
def btnselect_clicked():
    """ Function to merge all PDFs in a folder and cut the last pages.
    """
    pdf_list = select_all_pdfs()
    cut = int(spinNumber1.get())
    mergePDF(pdf_list,cut)
    
def btnOk2_clicked():
    x = entry3.get()
    y = entry4.get()
    cut_page1 = int(spinNumber2.get())
    cut_page2 = int(spinNumber3.get()) 
    mergingRandomName(x, y, cut_page1, cut_page2)

def btnConvt_clicked():
    x = entry5.get()
    pdfConvert(x)

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
window.geometry('1000x430')

# Add a vertical scrollbar to the window
# scrollbar = Scrollbar(window)
# scrollbar.pack(side="right", fill="y")  # Pack it on the right and fill vertically

# Scale it up so we can see it better...
window.tk.call('tk', 'scaling', 3.0)




#############
#   Widgets #
#############

# Concatenate PDFs in a folder
lbl = Label(window, text="Here you can Concatenate all PDFs in a Folder", font='Helvetica 9 bold')
lbl.grid(column=0, row=0, pady=5)

lbl = Label(window, text="Number of pages to cut at the End of each PDF: ")
lbl.grid(column=0, row=1, sticky="w", padx=5, pady=5)

cut_pages1 = StringVar()
spinNumber1 = Spinbox(window, from_=0, to=99, textvariable=cut_pages1)
spinNumber1.grid(column=1, row=1, pady=5)

btn_select_pdfs = Button(window, text="Select PDFs", command=btnselect_clicked)
btn_select_pdfs.grid(column=0, row=2, pady=5)

# Concatenate two PDFs
lbl = Label(window, text="Here you can Concatenate two PDFs", font='Helvetica 9 bold')
lbl.grid(column=0, row=3, pady=10)

lbl = Label(window, text="Select first: ")
lbl.grid(column=0, row=4, sticky="w", padx=5)

entry3 = Entry(window)
entry3.grid(column=1, row=4, padx=5)
entry3.bind("<Button-1>", lambda e: open_file_dialog(entry3))

lbl = Label(window, text="Number of pages to cut at the End: ")
lbl.grid(column=0, row=5, sticky="w", padx=5)

cut_pages2 = StringVar()
spinNumber2 = Spinbox(window, from_=0, to=99, textvariable=cut_pages2)
spinNumber2.grid(column=1, row=5, padx=5)

lbl = Label(window, text="Select second: ")
lbl.grid(column=0, row=6, sticky="w", padx=5)

entry4 = Entry(window)
entry4.grid(column=1, row=6, padx=5)
entry4.bind("<Button-1>", lambda e: open_file_dialog(entry4))

lbl = Label(window, text="Number of pages to cut at the End: ")
lbl.grid(column=0, row=7, sticky="w", padx=5)

cut_pages3 = StringVar()
spinNumber3 = Spinbox(window, from_=0, to=99, textvariable=cut_pages3)
spinNumber3.grid(column=1, row=7, padx=5)

btnOk2 = Button(window, text="Ok", command=btnOk2_clicked)
btnOk2.grid(column=0, row=8, pady=5)

# Conversion Section
lbl = Label(window, text="Convert a file to PDF", font='Helvetica 9 bold')
lbl.grid(column=0, row=9, pady=10)

entry5 = Entry(window)
entry5.grid(column=1, row=9, padx=5)
entry5.bind("<Button-1>", lambda e: open_file_dialog(entry5))

btnOk3 = Button(window, text="Convert", command=btnConvt_clicked)
btnOk3.grid(column=0, row=10, pady=5)

btnCancel = Button(window, text="Cancel", command=btnCancel_clicked)
btnCancel.grid(column=1, row=11, pady=10)

# Start the Tkinter event loop
window.mainloop()
