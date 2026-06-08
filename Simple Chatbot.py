from tkinter import *

def send():
    user_msg = "You: " + e.get()
    text.insert(END, "\n" + user_msg)
    
    if e.get() == 'hi':
        text.insert(END, "\n" + "Bot: hello")
    elif e.get() == 'hello':
        text.insert(END, "\n" + "Bot: hi")
    elif e.get() == 'how are you?':
        text.insert(END, "\n" + "Bot: i'm fine and you?")
    elif e.get() == "i'm fine too":
        text.insert(END, "\n" + "Bot: nice to hear that")
    else:
        text.insert(END, "\n" + "Bot: Sorry I didn't get it.")

root = Tk()
root.title('Simple Chatbot')

text = Text(root, bg='light blue')
text.grid(row=0, column=0, columnspan=2)

e = Entry(root, width=80)
e.grid(row=1, column=0)

Button(root, text='Send', bg='blue', width=20, command=send).grid(row=1, column=1)

root.mainloop()
