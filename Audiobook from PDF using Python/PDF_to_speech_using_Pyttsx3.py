# pyttsx3 is a text-to-speech conversion library in Python
import pyttsx3
# pypdf2 is an open source pure-python PDF library to read, split, crop, merge and transform 
# PDF files
import PyPDF2  


def audiobook_instant(pdf_loc):
    
    pdf = open(pdf_loc,'rb')
    reader = PyPDF2.PdfFileReader(pdf)
    num_pages = reader.numPages
    
    play = pyttsx3.init()
    print('Audio Book is playing now... Enjoy..')
    
    for num in range(0, num_pages):
        read_pages = reader.getPage(num)
        text = read_pages.extractText()
        
        play.say(text)
        play.runAndWait()
        

audiobook_instant('Frost.pdf')