from tkinter import *

top = Tk()
top.geometry("250x250")

def hello():
    text.insert(INSERT, "User: ")
    text.insert(INSERT, E1.get())
    text.insert(INSERT, "\n")
    text.pack()
    
Conversation = Text(top)

Send = Button(top, text ="Send", command = hello)
Phrase = Entry(top, bd = 5)
Phrase.pack()
Send.pack()
Conversation.pack()

top.mainloop()
