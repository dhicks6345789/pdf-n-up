import sys
#import math
import PyPDF2

if (len(sys.argv) != 4):
	print("Usage: python n-up.py layout inputFile outputFile")
	print("Layout can be one of: booklet, zine."
	sys.exit(1)
print()
inputPDF = pyPDF2.PdfFileReader(open(sys.argv[2], "rb"))
outputPDF = PdfFileWriter()
for pageNumber in range (0, inputPDF.getNumPages()-1):
	print(pageNumber)
#lhs = input1.getPage(iter)
#rhs = input1.getPage(iter+1)
#lhs.mergeTranslatedPage(rhs, lhs.mediaBox.getUpperRight_x(),0, True)
#output.addPage(lhs)
#print (str(iter) + " "),
#sys.stdout.flush()

#print("writing " + sys.argv[2])
#outputStream = file(sys.argv[2], "wb")
#output.write(outputStream)
#print("done.")