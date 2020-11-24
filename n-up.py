import sys
#import math
import PyPDF2

if (len(sys.argv) != 4):
	print("Usage: python n-up.py layout inputFile outputFile")
	print("Layout can be one of: booklet, zine.")
	sys.exit(1)
	
inputPDF = PyPDF2.PdfFileReader(open(sys.argv[2], "rb"))

outputPDF = PyPDF2.PdfFileWriter()
pageWidth = inputPDF.getPage(0).mediaBox[2] - inputPDF.getPage(0).mediaBox[0]
pageHeight = inputPDF.getPage(0).mediaBox[3] - inputPDF.getPage(0).mediaBox[1]
outputPage = outputPDF.addBlankPage(pageWidth, pageHeight)

for pageNumber in range (0, inputPDF.getNumPages()):
	print(str(pageNumber))
inputPage = inputPDF.getPage(0)
inputPage.scaleBy(0.25)
outputPage.mergeRotatedTranslatedPage(inputPage, 90, 0, 0, False)

outputHandle = open(sys.argv[3], "wb")
outputPDF.write(outputHandle)
