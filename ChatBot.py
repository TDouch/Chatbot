import nltk, re, pprint
from nltk import word_tokenize
import sys
import time
import random



def Error():
    Errors = ["Sorry, I did not understand that. Could you mabye reword that for me.", "Sorry, I could you be more specific", "I did not understand you message."]
    print(Errors[random.randint(0,2)])
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
    print("Oh , sorry I must have miss read your message.")
def Complete():
    time.sleep(1)
    print("hopefuly that has helped with the issue. Is there anything else I can help with?")
    x = 0
    InputPhrase()
    for i in Phrase:
        if i.lower() == "yes":
            x = 1
            print("What is the area of the next problem?")
            problem()
    if x == 0:
        sys.exit()
def Problem():
    InputPhrase()
    x=0
    for i in Phrase:
        if i.lower() == "hardware":
            x = 1
            print ("HW")
            HwArea()
        elif i.lower() == "software":
            x = 1
            print ("SW")
        elif i.lower() == "moodle":
            x = 1
            print ("MD")
            MdlArea()
        elif i.lower == "files" or i.lower == "storage":
            x = 1
            Files()
    if x == 0:
        Error()
        Problem()

def loop():
    print("Is there anything else I can try to help with?")
    Problem()


def MdlArea():

    print("what area of the moodle system are causeing these problems?")
    InputPhrase()
    x=0
    for i in Phrase:
        if i.lower() == "email" or i.lower() == "e-mail":
            x = 1
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
            x = 1
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
            x = 1
            print("You are having issues with you module pages, correct?")
            InputPhrase()
            for i in Phrase:
                if i.lower() =="yes":
                    MdlModule
                elif i.lower()== "no":
                    Sorry()
                    MdlArea()
        elif i.lower() == "timetable":
            x = 1
            print("There is an issue with your timetable?")
            InputPhrase()
            for i in Phrase:
                if i.lower() =="yes":
                    print("Issues with Timetables can be fixed by messaging Regisrty.")
                    sys.exit()
                elif i.lower()== "no":
                    Sorry()
        elif i.lower() == "down":
            x = 1
            print("Unforntunatly Moodle is hosted externaly from the university, and we have no control over the servers. They will be up again as soons as they can be.")
    if x == 0:
        Error()
        MdlArea()
def MdlModule():
    print("What part of Modules are not working.")
    InputPhrase()
    x=0
    for i in Phrase:
        if i.lower() == "missing":
            x = 1
            print("So some of your modules are missing from moodle?")
            InputPhrase()
            for i in Phraase:
                if i.lower() =="yes":
                    print("Check under other modules incase it is there, if not email registery as they will be able to sort it out.")
                    Complete()
                elif i.lower()== "no":
                    Sorry()
                    MdlArea()
        elif i.lower() == "extra":
            x = 1
            print("If there are any extra modules on the list, as long as they are not effecting anything they can be left there.")
            Complete()
    if x == 0:
        Error()
        MdlModule()
def SwArea():
    print("Are the software issues based around university software or software at home?")
    InputPhrase()
    x=0
    for i in Phrase:
        if i.lower() == "university" or i.lower() == "uni":
            x = 1
            SwUni()

        elif i.lower()== "home":
            x = 1
            SwHome()
    if x == 0:
        Error()
        SwArea()
def SwUni():
    print("Are you having issues with not being able to find software or is it an issue with the software itself?")
    InputPhrase()
    x=0
    for i in Phrase:
        if i.lower() == "missing":
            x = 1
            print("Some pieces of software are only avaibable from certain computer around the university. You may be able to find the software you need on the mylaunch system that should be on your desktop.")
            Complete()
        #####finish#####
    if x == 0:
        Error()
        SwUni()
#def SwHome():
        #####finish#####

def HwArea():
    print("what area of the hardware are causeing these problems?")
    InputPhrase()
    x=0
    for i in Phrase:
        if i.lower() == "printer":
            x = 1
            print("To use the printers at the university you need to make sure of a few things before you can successfuly print.")
            time.sleep(.5)
            print("You need to make sure that you have enough printer credits and that you have your student id")
            time.sleep(.5)
            print("If you have both of these then you send something tobe proiinted then login at the printer that you have sent it to.")
            time.sleep(.5)
            print("Did that solve the issue?")
            InputPhrase()
            for i in Phrase:
                if i.lower() == "credits":
                    print("IF you are out of credits more can be purchased online using a debit or credit card on FollowMe, via the Student Portal.")
                    Complete()
        elif i.lower() == "mouse" or i.lower() == "keyboard":
            x = 1
            print("If the mice or keyboards are not working it is best not to mess with the computer to try and get them working.")
            print("If they are completely missing unfortunatly all you can do is notify someone and move to another computer.")
            Complete()
        #####finish#####

def files():
    print("Is a file missing or are you trying to access you files from home?")
    InputPhrase()
    x=0
    for i in Phrase:
        if i.lower() == "missing":
            x = 1
            print("Unless set up correctly some programs may save to the Documents folder as default.")
            print("Were you able to find the files?")
            InputPhrase()
            for i in Phrase:
                if i.lower() == "yes":
                    print("Good to hear. Next time try to remember to organise your files properly")
                    Complete()
            print("If you were unable to find the files there may be a back-up on the servers, get in contact technical support.")
            Support()
        elif i.lower() == "home" or i.lower == "outside":
            x = 1
            print("To access your university files from home you can use remote desktop connection. Which should be installed on your home maciene as standard.")
            time.sleep(1)
            print("Use cu2study.coventry.ac.uk AS the computer to connect to, you will then be asked to login with you university login details to access your files.")
            time.sleep()
            Complete()

    if x == 0:
        Error()
        SwUni()

print("""Hello I Am a techincal support bot. Iam here to try and help with hardware,software, and moodle issues? Please state the are you are having issues with.""")
Problem()
