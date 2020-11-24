import sys
#import math
import PyPDF2

if (len(sys.argv) != 4):
	print("Usage: python n-up.py layout inputFile outputFile")
	print("Layout can be one of: booklet, zine.")
	sys.exit(1)
	
inputPDF = PyPDF2.PdfFileReader(open(sys.argv[2], "rb"))
outputPDF = PyPDF2.PdfFileWriter()
print(inputPDF.getPage(0).mediaBox[2])
#outputPage = outputPDF.addBlankPage()
for pageNumber in range (0, inputPDF.getNumPages()):
	print("A" + str(pageNumber) + "B")
outputPage = inputPDF.getPage(0)
outputPage.mergeTranslatedPage(inputPage, outputPage.mediaBox.getUpperRight_x(),0, True)
#output.addPage(lhs)
#print (str(iter) + " "),
#sys.stdout.flush()

#print("writing " + sys.argv[2])
#outputStream = file(sys.argv[2], "wb")
#output.write(outputStream)
#print("done.")
