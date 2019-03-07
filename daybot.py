from Tkinter import *
import aiml

master = Tk()
daybot = aiml.Kernel()
daybot.learn('simple.aiml')
input_user = StringVar()

def interaksi(event):
    kata = input_field.get()
    print"kata : "+(kata)
    response = daybot.respond(kata)
    print "daybot : "+ response
    
def balas():
    kata = input_field.get()
    print"kata : "+(kata)
    response = daybot.respond(kata)
    print "daybot : "+ response
    
def close_window():
    master.destroy()

title = Label(master, text="DayBOT")
title.pack(side=TOP)
title = Label(master, text="Teman Chat Jones")
title.pack(side=TOP)

input_field = Entry(master, text=input_user)
input_field.pack()

frame = Frame(master, width=100, height=60)
input_field.bind("<Return>", interaksi)
frame.pack()

button = Button (frame, text= "Balas", command = balas)
button.pack()

frame = Frame(master)
frame.pack()
button = Button (frame, text = "EXIT", command = close_window)
button.pack(side=BOTTOM)

master.mainloop()

