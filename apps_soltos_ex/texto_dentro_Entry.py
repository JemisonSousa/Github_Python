from tkinter import *


class AddLabelComFuncao:
    def __init__(self):
        self.root = Tk()

        self.texto_Entry = Entry(self.root, width=50)
        self.texto_Entry.pack()
        self.texto_Entry.insert(0, "Entre com seu texto")

        def myCalc():
            msg_a_ser_exibida = "Hello " + self.texto_Entry.get()
            myLabel = Label(self.root, text=msg_a_ser_exibida)
            myLabel.pack()

        self.myButton = Button(self.root, text="Entre com seu Stock", command=myCalc)
        self.myButton.pack()

        self.root.mainloop()


AddLabelComFuncao()