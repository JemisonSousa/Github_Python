# from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
# from tkinter.constants import BOTTOM
# from tkinter.ttk import Frame, Label, Entry

from tkinter import *
from tkinter import ttk, BOTH

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Review")
        self.pack(fill=BOTH, expand=True)

    
        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Título", width=6)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Autor", width=6)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)

        lbl3 = Label(frame3, text="Review", width=6)
        lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

        txt = Text(frame3)
        txt.pack(fill=BOTH, pady=5, padx=7, expand=True)

        # #------------------------------------------------------------
        #  #eu adicionando

        # titulo = frame1
        # autor = frame2
        # review = txt

        # frame4 = Frame(self)
        # frame4.pack(fill=X)
        # lbl4 = Label(frame4, text="O título é " + titulo + ".")
        # lbl4.pack()
        
    

        # #-----------------------------------------------------------


def main():

    root = Tk()
    root.geometry("300x300+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()