from msilib.schema import Error
from PyPDF3 import PdfFileReader, PdfFileWriter
from gtts import gTTS
import os

FILE = ''
NEW_FILE = ''
FINAL_FOLDER = '' + '/'


file = open(FILE, 'rb')
PdfReader = PdfFileReader(file)
book_info = PdfReader.getDocumentInfo()
# print(book_info)

def splitFile(page):
    PdfWriter = PdfFileWriter()
    PdfWriter.addPage(PdfReader.getPage(page))
    splitted_file_name = FINAL_FOLDER + NEW_FILE + str(page) + '.pdf'

    if not os.path.exists(splitted_file_name):
        SplitPdfFile = open(splitted_file_name, 'wb')
        PdfWriter.write(SplitPdfFile)
        SplitPdfFile.close()

    return splitted_file_name


def get_pdf_text(file):

    try:
        the_file = file
        PdfReader=PdfFileReader(the_file)
        pages_number = PdfReader.getNumPages()

        text_list=[]
        for i in range(pages_number):
            try:
                page = PdfReader.getPage(i)
                text_list.append(page.extractText())
            except Error as e:
                print(e)
        #Converting multiline text to single line text
        text_string = " ".join(text_list)

        return text_string
    except AttributeError as error:
        print(error)


def convert_text_to_mp3(text, lang, file_name):
    try:
        my_audio = gTTS(text=text, lang=lang, slow=False)
        my_audio.save(file_name)

    except Exception as exception:
        print(exception)


# filename = splitFile(11)
# text = get_pdf_text(filename)
# convert_text_to_mp3(text, 'en', 'audio.mp3')
