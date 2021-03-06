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

if sys.argv[1] == "zine":
	pageTransforms = [[scaledWidth*2,scaledHeight*3,90],[0,scaledHeight*4,270],[0,scaledHeight*3,270],[0,scaledHeight*2,270],[0,scaledHeight*1,270],[scaledWidth*2,0,90],[scaledWidth*2,scaledHeight*1,90],[scaledWidth*2,scaledHeight*2,90]]
	for pageNumber in range (0, inputPDF.getNumPages()):
		outputPage.mergeRotatedScaledTranslatedPage(inputPDF.getPage(pageNumber), pageTransforms[pageNumber][2], 0.3536, pageTransforms[pageNumber][0], pageTransforms[pageNumber][1])
else:
	print("Unknown layout: " + sys.argv[1])

outputPDF.write(open(sys.argv[3], "wb"))
