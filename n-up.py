import sys
import PyPDF2

if (len(sys.argv) != 4):
	print("Usage: python n-up.py layout inputFile outputFile")
	print("Layout can be one of: booklet, zine.")
	sys.exit(1)
	
inputPDF = PyPDF2.PdfFileReader(open(sys.argv[2], "rb"))

scaleFactor = 0.25
outputPDF = PyPDF2.PdfFileWriter()
pageWidth = inputPDF.getPage(0).mediaBox[2] - inputPDF.getPage(0).mediaBox[0]
scaledWidth = pageWidth * scaleFactor
pageHeight = inputPDF.getPage(0).mediaBox[3] - inputPDF.getPage(0).mediaBox[1]
scaledHeight = pageHeight * scaleFactor

outputPage = outputPDF.addBlankPage(pageWidth, pageHeight)

for pageNumber in range (0, inputPDF.getNumPages()):
	print(str(pageNumber))
inputPage = inputPDF.getPage(0)
inputPage.scaleBy(scaleFactor)
outputPage.mergeRotatedTranslatedPage(inputPage, 90, scaledWidth, scaledHeight, False)

outputHandle = open(sys.argv[3], "wb")
outputPDF.write(outputHandle)
