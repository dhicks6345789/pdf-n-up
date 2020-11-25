import sys
import PyPDF2

if (len(sys.argv) != 4):
	print("Usage: python n-up.py layout inputFile outputFile")
	print("Layout can be one of: booklet, zine.")
	sys.exit(1)
	
inputPDF = PyPDF2.PdfFileReader(open(sys.argv[2], "rb"))
pageWidth = inputPDF.getPage(0).mediaBox[2] - inputPDF.getPage(0).mediaBox[0]
scaledWidth = pageWidth / 2
pageHeight = inputPDF.getPage(0).mediaBox[3] - inputPDF.getPage(0).mediaBox[1]
scaledHeight = pageHeight / 4

outputPDF = PyPDF2.PdfFileWriter()
outputPage = outputPDF.addBlankPage(pageWidth, pageHeight)

pageTransforms = [[scaledWidth*2,scaledHeight*4,90],[scaledWidth,scaledHeight*4,270],[0,0,270],[0,0,270],[0,0,90],[0,0,90],[0,0,90],[0,0,90]]
for pageNumber in range (0, inputPDF.getNumPages()):
	if pageNumber <= 1:
		outputPage.mergeRotatedScaledTranslatedPage(inputPDF.getPage(pageNumber), pageTransforms[pageNumber][2], 0.3536, pageTransforms[pageNumber][0], pageTransforms[pageNumber][1])

outputPDF.write(open(sys.argv[3], "wb"))
