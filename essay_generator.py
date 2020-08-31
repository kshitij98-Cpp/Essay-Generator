'''
Please read this steps before running the project!!

1. Please Turn off or Disable pylint before starting this project.
2. In VSCode you can do this by "ctrl+shift+p" and type pylint and disable it.
2. And install webdriver of your browser(what ever you use) and paste it in your python directory.
'''

''' If the GUI is showing "not responding" don't close the program,it is doing its' process, since pyqt works on 'queue' which means one-by-one the process will get executed. '''

import time
from selenium import webdriver
import sys
import os
import playsound
import pyaudio

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtTest
from Button import *
from gtts import gTTS
import speech_recognition as sr

#gtts for giving introduction
def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "sample2.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
speak("Hello,welcome to Essay Generator.Before starting make sure you have installed all dependencies mentioned in Read Me on Github.Please Vote this project if you liked it.This is my first project in python and there is a least chance it will get selected, anyways thanks. All the best everyone. The audio playback may take some time depending on the length of the essay. It all depends on the speed of Internet Connection.")


#Method for stop or start the playback according to user
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)

        except Exception as e:
            speak("I didn't understand")
    return said
    

# Created class having parameter 'QMainWindow" 


class make(QMainWindow):

    def __init__(self, parent = None):
        super(make, self).__init__(parent)
        self.ui = Ui_Essay_Generator()
        self.ui.setupUi(self)

        #When the pushButton gets clicked, function 'create' will get executed
        self.ui.generate.clicked.connect(self.create)
    
        self.show()


    def create(self):
        #Grab the content of comboBox and assign it to string variable 'b'
        b = str(self.ui.comboBox.currentText())
        
        #Checks the name of Browser entered by the user
        if(b == "Chrome"):


            options = webdriver.ChromeOptions()

            #argument ("--headless") will give browser instruction to process the work in background
            options.add_argument("--headless")

            options.add_argument("--disable-gpu")

            #initialised the driver
            driver = webdriver.Chrome(options=options)
            
            #Grab the content of LineEdit and assign the value to 'search'
            search = str(self.ui.getText.text())
            
            #mod_search will replace the 'white space' with '_' to make the search efficient.
            mod_search = search.replace(" ", "_")

            # 'driver.get' will give instruction the browser to open the webpage
            driver.get(f"https://en.wikipedia.org/wiki/{mod_search}")

            #Created a file
            output =  open(fr"{mod_search}_essay.txt", "w+", encoding = "utf-8") 

            # Verifying the condition
            if "Wikipedia does not have an article with this exact name."in driver.page_source:

                self.ui.Result.setText("Sorry we don't generate garbage.\nYour spelling might be wrong or the word you entered, please correct\n and try again.")


            else:
                #This will search the all the content which are enclosed by id
                para = driver.find_element_by_id("bodyContent")

                #This will search the all the content which are assigned with tag name <p> stands for paragraph in html
                p_tags = para.find_elements_by_tag_name("p")

                #Using for loop to get all the content
                for p_tag in p_tags:
                    #Writing to the file saved as .txt
                    output.write(f"\t{p_tag.text}\n\n")

                #Assigning the completion to label.
                self.ui.Result.setText(f"Process Completed. Essay saved in {mod_search}_essay.txt")
                
                #Delaying the GUI process for 3 seconds. 
                QtTest.QTest.qWait(3000)

                self.ui.Result.setText("Audio Playback may take some time, be patient.\nMake sure internet is enabled")
                
                QtTest.QTest.qWait(3000)
                self.ui.Result.setText("If you want to stop playback and don't want to listen say 'stop' \n after the speaker says 'playback started'\n if u want to listen say 'start'. ")
                QtTest.QTest.qWait(1000)
                #closing the file
                output.close()
                
                
                
                '''gTTS for conversion of .txt to .mp3. This all depends on the speed of Internet Connection, faster the internet,faster the conversion.'''              
                file = open(f"{mod_search}_essay.txt","r", encoding = "utf-8").read().replace("\n", " ")
                speech = gTTS(text = str(file), lang = 'en', slow= False)
                filename = "essay.mp3"
                #saving the .mp3 as "essay.mp3"
                speech.save(filename)

                time.sleep(2)
                #Using the playsound module to play .mp3 files
                speak("playback is starting. If you want to start say start and if you don't want to listen the playback say stop, after i stop saying anything.")
                text = get_audio()
                if str("stop") in text:
                    print("Process stopped.\n")
                    exit(0)
                elif str("start") in text:
                    playsound.playsound(filename)
                 
                

         
        if (b == "Firefox"):
            
            
            options = webdriver.FirefoxOptions()
            #argument ("--headless") will give browser instruction to process the work in background
            options.add_argument("-headless")

            #initialised the driver
            driver = webdriver.Firefox(options=options)

            #Grab the content of LineEdit and assign the value to 'search'
            search = str(self.ui.getText.text())

            #mod_search will replace the 'white space' with '_' to make the search efficient.
            mod_search = search.replace(" ", "_")
            
            # 'driver.get' will give instruction the browser to open the webpage
            driver.get(f"https://en.wikipedia.org/wiki/{mod_search}")

            #Created a file
            output =  open(f"{mod_search}_essay.txt", "w+", encoding = "utf-8")

            # Verifying the condition
            if "Wikipedia does not have an article with this exact name."in driver.page_source:

                self.ui.Result.setText("Sorry we don't generate garbage.Your spelling might be wrong or the word you entered, please correct.")

            else:
                #This will search the all the content which are enclosed by id
                para = driver.find_element_by_id("bodyContent")

                #This will search the all the content which are assigned with tag name <p> stands for paragraph in html
                p_tags = para.find_elements_by_tag_name("p")

                #Using for loop to get all the content
                for p_tag in p_tags:

                    #Writing to the file saved as .txt
                    output.write(f"\t{p_tag.text}\n\n")

                #Assigning the completion to label.
                self.ui.Result.setText(f"Process Completed. Essay saved in {mod_search}_essay.txt")

                QtTest.QTest.qWait(3000)

                self.ui.Result.setText("Audio Playback may take some time, be patient.\nMake sure internet is enabled")

                QtTest.QTest.qWait(3000)
                self.ui.Result.setText("If you want to stop playback and don't want to listen say 'stop' \n after the speaker says 'playback started'\n if u want to listen say 'start'. ")
                
                QtTest.QTest.qWait(1000)
                #closing the file
                output.close()

                #gtts for conversion

                file = open(f"{mod_search}_essay.txt","r", encoding = "utf-8").read().replace("\n", " ")

                speech = gTTS(text = str(file), lang = 'en', slow= False)

                filename = "essay.mp3"
                #saving the .mp3 as "essay.mp3"
                speech.save(filename)

                time.sleep(2)
                #Using the playsound module to play .mp3 files
                speak("playback is starting. If you want to start say start and if you don't want to listen the playback say stop, after i stop saying anything.")
                text = get_audio()
                if "stop" in text:
                    print("Process stopped.\n")
                    exit(0)
                elif "start" in text:
                    playsound.playsound(filename)


            
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = make()
    w.show()
    sys.exit(app.exec_())





    


