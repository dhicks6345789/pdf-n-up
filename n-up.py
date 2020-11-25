import sys
import PyPDF2

if (len(sys.argv) != 4):
	print("Usage: python n-up.py layout inputFile outputFile")
	print("Layout can be one of: booklet, zine.")
	sys.exit(1)
	
inputPDF = PyPDF2.PdfFileReader(open(sys.argv[2], "rb"))

outputPDF = PyPDF2.PdfFileWriter()
pageWidth = inputPDF.getPage(0).mediaBox[2] - inputPDF.getPage(0).mediaBox[0]
scaledWidth = pageWidth / 2
pageHeight = inputPDF.getPage(0).mediaBox[3] - inputPDF.getPage(0).mediaBox[1]
scaledHeight = pageHeight / 4

print(pageHeight)
print(scaledHeight)

outputPage = outputPDF.addBlankPage(pageWidth, pageHeight)

pageTransforms = [[300,0,270],[0,0,90],[0,0,90],[0,0,90],[0,0,270],[0,0,270],[0,0,180],[0,0,180]]
for pageNumber in range (0, inputPDF.getNumPages()):
	inputPage = inputPDF.getPage(pageNumber)
	inputPage.scaleBy(0.25)
	outputPage.mergeRotatedTranslatedPage(inputPage, pageTransforms[pageNumber][2], pageTransforms[pageNumber][0], pageTransforms[pageNumber][1], False)

outputHandle = open(sys.argv[3], "wb")
outputPDF.write(outputHandle)
