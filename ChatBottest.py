import nltk, re, pprint
from nltk import word_tokenize
import sys
import time
import random

ChatLog = open('ChatLog', 'w')

keywords = [['moodle', 'login', 'email', 'modules', 'missing', 'extra', 'coursework', 'timetable', 'down'],
            ['software', 'university', 'uni', 'home', 'missing', 'files', 'save', 'crash'],
            ['hardware', 'printer', 'credits', 'periferals', 'mouse', 'keyboard']]

def Error():
    Errors = ["Sorry, I did not understand that. Could you mabye reword that for me.", "Sorry, I could you be more specific", "I did not understand you message."]
    print(Errors[random.randint(0,2)])
    ChatLog.write("Message from user not understood: ")
    ChatLog.write(" ".join(Phrase))
    ChatLog.write("\n")
def InputPhrase():
    global Phrase
    Phrase = word_tokenize(input('User: ').lower())
    cp = nltk.RegexpParser("""NT: {<RB><IN><NN>}
                           NP: {<DT>?<JJ>*<NN>}
                           VB: {<VBP>?<VB>*<VBG>}""")
    result = cp.parse(nltk.pos_tag(Phrase))
    print (result)
    if "staff" and "direct" in Phrase:
        Support()
    x=0
    try:
        for i in result:
            if result[x].label() == "NT":
                print (result[x].label())
                print (result[x])
                for i in result[x]:
                    if "hardware" in i or "moodle" in i or "software" in i:
                        print ("Okay, what are is the issue occuring from?")
                        Problem()
            x+=1
    except AttributeError:
        print("")
    
    #print (result[1])
    #result.draw()
        
            
def Support():
    print("Here is the contact information for technical support.")
    ChatLog.write("Passed onto support staff.")
    ChatLog.close()
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
        ChatLog.close()
        sys.exit()
def Problem():
    InputPhrase()
    x=0
    for i in Phrase:
        if i.lower() == keywords[2][0]:
            x = 1
            ChatLog.write("Problem Area: Hardware\n")
            HwArea()
        elif i.lower() == keywords[1][0]:
            x = 1
            ChatLog.write("Problem Area: Software\n")
            SwArea()
        elif i.lower() == keywords[0][0]:
            x = 1
            ChatLog.write("Problem Area: Moodle\n")
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
    if any(x in keywords[0] for x in Phrase):
        for i in Phrase:
            if i.lower() == "email" or i.lower() == "e-mail":
                print("You are having an issues with the univiersity email?")
                InputPhrase()
                for i in  Phrase:
                    if i.lower() == "yes":
                        ChatLog.write("Issue with 'the email system\n")
                        ChatLog.write(" ".join(Phrase))
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
                        ChatLog.write("Issue with the moodle login\n'")
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
                        ChatLog.write("Issue with the modules page\n'")
                        ChatLog.write(" ".join(Phrase))
                        MdlModule()
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
            elif i.lower() == "down":
                print("Unforntunatly Moodle is hosted externaly from the university, and we have no control over the servers. They will be up again as soons as they can be.")
    else: 
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
    x = 0
    for i in Phrase:
        if i.lower() == "missing":
            x = 1
            print("Some pieces of software are only avaibable from certain computer around the university. You may be able to find the software you need on the mylaunch system that should be on your desktop.")
            Complete()
        elif i.lower() =="files" or i.lower =="save":
            x = 1
            Files()
    if x == 0:
        Error()
        SwUni()
def SwHome():
    print("I will try to help as best as I can but many pieces of software I will not be able to help in detail.")
    print("Most fixes will be general to most piseces of software.")
    InputPhrase()
    x = 0
    for i in Phrase:
        if i.lower() == "crash":
            x = 1
            print("If the program keeps on crashing attempting to run it in admistrator mode, or if it is an older piece of software you may need to set it in compatability mode. The setting for this are in the poperties option when you right-click the software.")
            time.sleep(1)
            print("If this did not work try uninstalling the software and then re-installing it afresh.")
            Complete()
        #####finish#####
def HwArea():
    print("what area of the hardware are causeing these problems?")
    InputPhrase()
    if any(x in keywords[2] for x in Phrase):
        for i in Phrase:
            if i.lower() == "printer" or i.lower() == "printers":
                print("To use the printers at the university you \nneed to make sure of a few things before \nyou can successfuly print.\n")
                time.sleep(1)
                print("You need to make sure that you have enough \nprinter credits and that you have your \nstudent id.\n")
                time.sleep(1)
                print("If you have both of these then you send \nsomething to be printed. Tthen login at the \nprinter that you have sent it to.\n")
                time.sleep(1)
                print("Did that solve the issue?")
                InputPhrase()
                for i in Phrase:
                    if i.lower() == "yes":
                        Complete()
                    elif i.lower() == "credits":
                        print("If you are out of credits more can be purchased online using a debit or credit card on FollowMe, via the Student Portal.")
                        Complete()
            elif i.lower() == "mouse" or i.lower() == "keyboard":
                print("If the mice or keyboards are not working it is best not to mess with the computer to try and get them working.")
                print("If they are completely missing unfortunatly all you can do is notify someone and move to another computer.")
                Complete()
        #####finish#####
    else:
        Error()
        HwArea()
def Files():
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
ChatLog.close()
