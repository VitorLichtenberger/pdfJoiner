
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
def merge_helper(pdfs):
    #Merging
    merger = PdfWriter()

    for pdf in pdfs:
    
        pdfReader = PyPDF2.PdfReader(pdf)
        max = len(pdfReader.pages) 
        merger.append(pdf, pages=(0,max-1))

    merger.write("res.pdf")
    merger.close()
    

def mergePDF(anfang, ende):
    """Funktion is suposed to merge a multiple number of PDFs all with beginning 01-XX.pdf

    Args:
        anfang (Int): Start of the PDFs
        ende (Int): End of PDFs
    """
    pdf_list = listHelper(anfang,ende)
    
    merge_helper(pdf_list)

def mergingRandomName(pdf1, pdf2):
     """Suposed to merge to randomly named pdfs leaving out last page.
    
     Args:
         pdf1 (String): Merging PDF
         pdf2 (String): Merging PDF
     """
     merger = PdfWriter()
    
     pdfReader = PyPDF2.PdfReader(pdf1)
     max1 = len(pdfReader.pages) 
     merger.append(pdf1, pages=(0,max1))
    
     pdfReader = PyPDF2.PdfReader(pdf2)
     max2 = len(pdfReader.pages) 
     merger.append(pdf2, pages=(0,max2))

     merger.write("randomMerge.pdf")
     merger.close()

