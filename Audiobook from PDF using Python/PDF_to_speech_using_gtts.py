#gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google 
#Translate text-to-speech API
from gtts import gTTS
import PyPDF2


# article = """
# This side Abhinav, providing a short tutorial on Text to Speech generator programming 
# on python
# """
book = open('Frost.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(book)
num_pages = pdf_reader.numPages

language = 'en'
text = " "
for num in range(0, num_pages):
	page = pdf_reader.getPage(num)
	text = text + page.extractText() #To add all the text in one place

#print(text)
gtts_transformer = gTTS(text=text, lang=language)
gtts_transformer.save("Robert_Frost_Poem.mp3")
print("WORK DONE")