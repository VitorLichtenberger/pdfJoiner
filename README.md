# pdfJoiner
This program allows you to merge PDFs in two ways:

-Merge all PDFs in a folder or Merge two PDFs from different directories

In both cases, you can choose how many pages should be removed from the end.
The output file will be created in the same folder where the program is executed.
The executable file (EXE) can be found in the dist folder.

Packages im using:

pip install pypdf
pip install PyPDF2
pip install pyinstaller
pip install tk
pip install fpdf
pip install python-docx


Usefull:

https://tkdocs.com/
https://docs.python.org/3/library/tk.html

Making EXE:
pyinstaller --onefile -w 'filename.py'
