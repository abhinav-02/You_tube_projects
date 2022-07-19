# pyttsx3 is a text-to-speech conversion library in Python
import pyttsx3
# pypdf2 is an open source pure-python PDF library to read, split, crop, merge and transform 
# PDF files
import PyPDF2  

book = open('Frost.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(book)
num_pages = pdf_reader.numPages

play = pyttsx3.init()
print('Playing Audio Book')

for num in range(0, num_pages):
	page = pdf_reader.getPage(num)
	data = page.extractText()

	play.say(data)
	play.runAndWait()