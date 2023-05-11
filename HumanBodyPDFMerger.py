# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 05:10:50 2022

@author: Mcrye
"""

import PyPDF2
 
# Open the files that have to be merged one by one
pdf1File = open(r'C:\Users\Mcrye\Documents\Personal\School\Spring2022\Seminar\Physics of Human Body\Physics of Human Body\Apendix Amathprm.pdf', 'rb')
pdf2File = open(r'C:\Users\Mcrye\Documents\Personal\School\Spring2022\Seminar\Physics of Human Body\Physics of Human Body\C0 preface.pdf', 'rb')
pdf3File = open(r'C:\Users\Mcrye\Documents\Personal\School\Spring2022\Seminar\Physics of Human Body\Physics of Human Body\C1 newton.pdf', 'rb')
pdf4File = open(r'C:\Users\Mcrye\Documents\Personal\School\Spring2022\Seminar\Physics of Human Body\Physics of Human Body\C2 scaling.pdf', 'rb')
pdf6File = open(r'C:\Users\Mcrye\Documents\Personal\School\Spring2022\Seminar\Physics of Human Body\Physics of Human Body\C3 musculo.pdf', 'rb')
pdf7File = open(r'C:\Users\Mcrye\Documents\Personal\School\Spring2022\Seminar\Physics of Human Body\Physics of Human Body\C4 fluids.pdf', 'rb')
pdf8File = open(r'C:\Users\Mcrye\Documents\Personal\School\Spring2022\Seminar\Physics of Human Body\Physics of Human Body\C6 thermo.pdf', 'rb')
pdf9File = open(r'C:\Users\Mcrye\Documents\Personal\School\Spring2022\Seminar\Physics of Human Body\Physics of Human Body\C7 brownian.pdf', 'rb')
pdf10File = open(r'C:\Users\Mcrye\Documents\Personal\School\Spring2022\Seminar\Physics of Human Body\Physics of Human Body\C9 excite.pdf', 'rb')
pdf11File = open(r'C:\Users\Mcrye\Documents\Personal\School\Spring2022\Seminar\Physics of Human Body\Physics of Human Body\C10 hearing.pdf', 'rb')
pdf12File = open(r'C:\Users\Mcrye\Documents\Personal\School\Spring2022\Seminar\Physics of Human Body\Physics of Human Body\C11 vision.pdf', 'rb')
pdf13File = open(r'C:\Users\Mcrye\Documents\Personal\School\Spring2022\Seminar\Physics of Human Body\Physics of Human Body\C12 rad_eff.pdf', 'rb')
pdf14File = open(r'C:\Users\Mcrye\Documents\Personal\School\Spring2022\Seminar\Physics of Human Body\Physics of Human Body\C13 diagnose.pdf', 'rb')
pdf15File = open(r'C:\Users\Mcrye\Documents\Personal\School\Spring2022\Seminar\Physics of Human Body\Physics of Human Body\toc.pdf', 'rb')

 
# Read the files that you have opened
j = 1
while j < 16:
    pdfjReader = PyPDF2.PdfFileReader(pdf+str(j)+File)

# Create a new PdfFileWriter object which represents a blank PDF document
pdfWriter = PyPDF2.PdfFileWriter()
 
i = 1
while i < 16:
    # Loop through all the pagenumbers for doc 1
    for pageNum in range(pdf+str(i)+Reader.numPages):
        pageObj = pdf+str(i)+Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    i += 1
 
# Now that you have copied all the pages in both the documents, write them into the a new document
pdfOutputFile = open('Physics of the Human Body.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
 
# Close all the files - Created as well as opened
pdfOutputFile.close()
n = 1
while n < 16:
    pdf+str(n)+File.close()
    n +=1 
