from tkinter import *

class MinhaFrame(Frame):
    def __init__(self, parent):
        super().__init__()

        self["bd"] = 1
        self["relief"] = SOLID

        self.text1_text = StringVar()
        self.label1_text = StringVar()

        #widgets
        self.label1 = Label(self, textvariable=self.label1_text).grid()
        text1 = Entry(self, textvariable=self.text1_text).grid()
        cmd1 = Button(self, text="Clique", command=self.Executar).grid()

    def Executar(self):
        self.label1_text.set("Olá " + self.text1_text.get() + ".")

root = Tk()
root.title("Uso de Clase e Frames")
# root.geometry("300x150")

frm1 = MinhaFrame(root).grid(row=0, column=0)
frm2 = MinhaFrame(root).grid(row=0, column=1)
frm3 = MinhaFrame(root).grid(row=1, column=0)
frm4 = MinhaFrame(root).grid(row=1, column=1)

root.mainloop()