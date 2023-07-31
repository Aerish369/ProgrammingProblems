from PyPDF2 import PdfMerger

files = ["Bermuda.pdf", "French Revolution.pdf", "Rana.pdf"] # Listing path of pdfs

merge = PdfMerger() # Creating object of PdfMerger() class

for file in files: # Iterating through files list
    merge.append(file) # Appending pdfs in merge object

merge.write("Merged.pdf") # writing the data into "Merged.pdf"
merge.close() # Closing the object like good programmer


