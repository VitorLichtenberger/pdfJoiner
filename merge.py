from PIL import Image
from fpdf import FPDF
from docx import Document
import os
from pypdf import PdfWriter

import PyPDF2

def listHelper(x,y):
    """Helper Funktion to create list of PDFs

    Args:
        x (Int): Beginning
        y (Int): End

    Returns:
        List: List of PDFs
    """
    #Creating list of pdfs
    pdfs = []
    j=1
    for i in range(x,y+1):
        if i <= 9 :
            pdfs.append("0"+ str(j) + ".pdf")
        else:
            pdfs.append(str(j) + ".pdf")
        j += 1
    return pdfs

def mergePDF(pdf_list, cut):
    """Funktion is suposed to merge a multiple number of PDFs in the list. Cuts number of pages at the end.

    Args:
        pdf_list (List): List of PDFs to merge.
        cut (Int) : Numger of Pages to cut at the end.
    """
    #pdf_list = listHelper()
    merger = PdfWriter()

    for pdf in pdf_list:
    
        pdfReader = PyPDF2.PdfReader(pdf)
        max = len(pdfReader.pages) 
        merger.append(pdf, pages=(0,max-cut))

    merger.write("foldermerge.pdf")
    merger.close()

def mergingRandomName(pdf1, pdf2, cut_page1, cut_page2):
     """Suposed to merge to randomly selected pdfs. And cut the Pages at the end acording to the input.
    
     Args:
         pdf1 (String): Merging PDF
         pdf2 (String): Merging PDF
         cut_page1 (Int): Number of Pages to cut pdf1
         cut_page2 (Int): Number of Pages to cut pdf2
         
     """
     merger = PdfWriter()
    
     pdfReader = PyPDF2.PdfReader(pdf1)
     max1 = len(pdfReader.pages) 
     merger.append(pdf1, pages=(0,max1-cut_page1))
    
     pdfReader = PyPDF2.PdfReader(pdf2)
     max2 = len(pdfReader.pages) 
     merger.append(pdf2, pages=(0,max2-cut_page2))

     merger.write("twoPDFmerge.pdf")
     merger.close()

def pdfConvert(conv):
    """Converts a jpg, Word (.docx), or text (.txt) file to a PDF and saves it in the same folder.

    Args:
        conv (str): Path to the file.
    """
    # Get the file extension and base name
    file_path, file_ext = os.path.splitext(conv)
    output_pdf = file_path + ".pdf"

    try:
        # Handle image files
        if file_ext.lower() in [".jpg", ".jpeg", ".png"]:
            image = Image.open(conv)
            rgb_image = image.convert("RGB")  # Ensure compatibility
            rgb_image.save(output_pdf)
            print(f"Image file converted and saved as {output_pdf}")
        
        # Handle Word documents
        elif file_ext.lower() == ".docx":
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            doc = Document(conv)
            for para in doc.paragraphs:
                pdf.multi_cell(0, 10, para.text)
            pdf.output(output_pdf)
            print(f"Word document converted and saved as {output_pdf}")
        
        # Handle text files
        elif file_ext.lower() == ".txt":
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            with open(conv, "r", encoding="utf-8") as file:
                for line in file:
                    pdf.multi_cell(0, 10, line.strip())
            pdf.output(output_pdf)
            print(f"Text file converted and saved as {output_pdf}")
        
        else:
            print("Unsupported file format. Please provide a .jpg, .docx, or .txt file.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
pdf = pdfConvert("Grid.JPG")