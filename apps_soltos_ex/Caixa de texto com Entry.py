from tkinter import *
from tkinter.messagebox import showinfo

def reply(name):
    #showinfo(title='Reply', message='Hello %s!' % name)
    showinfo('Reply', 'Hello %s!' % name)


top = Tk()
#img = PhotoImage(file='py-blue-trans-out.ico') #no

top.title('Echo')
#top.iconbitmap('icodoc.ico') #yes
#top.iconphoto(True, PhotoImage(file='tool.xbm')) #no

Label(top, text="Enter your name:").pack(side=TOP)
ent = Entry(top)
ent.pack(side=TOP)
btn = Button(top, text="Submit", command=(lambda: reply(ent.get())))
btn.pack(side=LEFT)

top.mainloop()