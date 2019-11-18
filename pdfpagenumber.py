from PyPDF2 import PdfFileReader
import glob
d=glob.glob("E:\\cats project\\CEDR_I_71_06_P\\*.pdf")
for x in d:
    pdf = PdfFileReader(open(x,'rb'))
    print(pdf.getNumPages())
