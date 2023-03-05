import os, time
from bs4 import BeautifulSoup
from deep_translator import *   # googletrans lib works buggy

rootPath = 'C://Users//alper//Documents//PycharmProjects//CodingAllstars//html_files'  # defined path for html nested folders


for dirPath, dirnames, fileNames in os.walk(rootPath):  # scans the entire depth of rootPath variable
    for filename in fileNames:
        print(filename)    # just to ensure file is readed
        if filename.endswith('.html'):
            filepath = os.path.join(dirPath, filename)
            with open(filepath, 'r+', encoding='utf-16') as f:
                html_content = f.read()
            soup = BeautifulSoup(html_content, 'html.parser')

            
            for element in soup.find_all(text=True):
                print(element)   # printing any text based element in html files 
                if element=='\n' or element[0]=='@' or element[0]=='{':  # skipping blank lines and html structures such as body etc.
                    continue
                try:
                    translated_text = GoogleTranslator(source='auto', target='hindi').translate(text=element)
                    print(translated_text)   # at this point, I managed to read the translated text in Hindi
                    html_content=html_content.replace(element, translated_text)
                except:
                    time.sleep(2)   # adding delay in case of html 403 error
                    continue

            translated_filepath = os.path.join(dirPath, 'translated_' + filename)  # Saving the translated HTML file

            with open(translated_filepath, 'w') as f:
                f.write(html_content)