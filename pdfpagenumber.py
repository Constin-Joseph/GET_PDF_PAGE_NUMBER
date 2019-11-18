from PyPDF2 import PdfFileReader
import glob
d=glob.glob("PATH\\*.pdf")
for x in d:
    pdf = PdfFileReader(open(x,'rb'))
    print(pdf.getNumPages())
