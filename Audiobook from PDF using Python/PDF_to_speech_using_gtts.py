#gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google 
#Translate text-to-speech API
from gtts import gTTS
# pypdf2 is an open source pure-python PDF library to read, split, crop, merge and transform 
# PDF files
import PyPDF2


def audiobook_text(text,save_location,lang = 'en'):
    '''
     Convert input text into speech.

    This function simply converts text input into speech

    Parameters
    ----------
    text : string
        The text which will be converted into speech
    save_location : string (ends with .mp3)
        where and with which name you wants to save it(it should end with .mp3)
                e.g. "abhinav.mp3"
    lang : string
        The language of the text
    Returns
    -------
    mp3 file
        The audio mp3 file will contains the speech of the input text
    '''
    gtts_transformer = gTTS(text=text, lang=lang)
    gtts_transformer.save(save_location)
    print("Audiobook is created. Check it out")
    
   
    

text = """
This side Abhinav, providing a short tutorial on Text to Speech generator programming 
on python
"""
save_location = "test.mp3"
audiobook_text(text, save_location)



def audiobook_pdf(pdf_location,save_location,lang = 'en'):
    '''
     Convert input text into speech.

    This function simply converts pdf input into speech

    Parameters
    ----------
    pdf_location : string
        location of pdf (ends with .pdf)
    save_location : string (ends with .mp3)
        where and with which name you wants to save it(it should end with .mp3)
                e.g. "abhinav.mp3"
    lang : string
        The language of the text
    Returns
    -------
    mp3 file
        The audio mp3 file will contains the speech of the input text
    '''
    pdf = open(pdf_location,'rb')
    reader = PyPDF2.PdfFileReader(pdf)
    num_pages = reader.numPages
    text = " "
    for num in range(0, num_pages):
        page = reader.getPage(num) 
        text = text + page.extractText()
    gtts_transformer = gTTS(text=text, lang=lang)
    gtts_transformer.save(save_location)
    print("Audiobook is created. Check it out")

audiobook_pdf('Frost.pdf', 'Frost.mp3')