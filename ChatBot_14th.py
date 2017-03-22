import nltk, re, pprint
from nltk import word_tokenize
import sys
import time

Errors = ["Sorry, I did not understand that. Could you mabye reword that for me.", "Sorry, I could you be more specific", "I did not understand you message."]


print (Errors[0])
def InputPhrase():
    global Phrase
    Phrase = word_tokenize(input('User: '))
    cp = nltk.RegexpParser("""NP: {<DT>?<JJ>*<NN>}
                           VB: {<VBP>?<VB>*<VBG>}""")
    result = cp.parse(nltk.pos_tag(Phrase))
    print (result)
    result.draw()

def Support():
    print("Here is the contact information for technical support.")
    sys.exit()

def Sorry():
    print("Oh , sorry i must have miss read your message.")

def Problem():
    print("""Hello I Am a techincal support bot.
          I am here to try and help with hardware,
          software, and moodle issues? Please state
          the are you are having issues with.""")
    InputPhrase()
    for i in Phrase:
        if i.lower() == "hardware":
            print ("HW")
        elif i.lower() == "software":
            print ("SW")
        elif i.lower() == "moodle":
            print ("MD")
            MdlArea()


def MdlArea():
    
    print("what area of the moodle system are causeing these problems?")
    InputPhrase()
    for i in Phrase:
        if i.lower() == "email" or i.lower() == "e-mail":
            print("You are having an issues with the univiersity email?")
            InputPhrase()
            for i in  Phrase:
                if i.lower() == "yes":
                    print("There is not much I can help with, all I can do is remind you of the address format: uni.coventry.ac.uk and that the password has a uppercase and a symbol.")
                    Support()
                    time.sleep(1.5)
                elif i.lower == "no":
                    Sorry()
                    MdlArea()
        elif i.lower() == "login" or i.lower() == "logging":
            print("You are having issues loggin into Moodle?")
            InputPhrase()
            for i in Phrase:
                if i.lower() =="yes":
                    print("There is not much I can help with, all I can do is remind you of the login format: name+initial+number and that the password has a uppercase and a symbol.")
                    Support()
                    time.sleep(1.5)
                elif i.lower()== "no":
                    Sorry()
                    MdlArea()
        elif i.lower() == "modules":
            print("You are having issues with you module pages, correct?")
            InputPhrase()
            for i in Phrase:
                if i.lower() =="yes":
                    MdlModule
                elif i.lower()== "no":
                    Sorry()
                    MdlArea()
        elif i.lower() == "timetable":
            print("There is an issue with your timetable?")
            InputPhrase()
            for i in Phrase:
                if i.lower() =="yes":
                    print("Issues with Timetables can be fixed by messaging Regisrty.")
                    sys.exit()
                elif i.lower()== "no":
                    Sorry()
                    
def MdlModule():
    print("What part of Modules are not working.")
    InputPhrase()
    for i in Phrase:
        if i.lower() == "missing":
            print("So some of your modules are missing from moodle?")
            InputPhrase()
            for i in Phraase:
                if i.lower() =="yes":
                    print("Check under other modules incase it is there, if not email registery as they will be able to sort it out.")
                elif i.lower()== "no":
                    Sorry()
                    MdlArea()
        
    
Problem()
