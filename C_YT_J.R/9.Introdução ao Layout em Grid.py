from tkinter import *
from tkinter import ttk

app = Tk()
app.title("GRID")
# app.geometry("500x500")
# app.geometry("%dx%d+%d+%d" % (500, 300, ((app.winfo_screenwidth())/2 - 500/2), ((app.winfo_screenheight())/2 - 300/2)))
app.iconbitmap("Ico-Fig-doc\carOfic.ico")

label_1 = Label(app, text="labal 1", font="Arial 20", bg="red")
label_2 = Label(app, text="labal 2", font="Arial 20", bg="green")
label_3 = Label(app, text="labal 3", font="Arial 20", bg="blue")

label_1.grid(row=0, column=0)
label_2.grid(row=0, column=1)
label_3.grid(row=0, column=2)

btn_1 = ttk.Button(app, text="Click_1")
btn_2 = Button(app, text="Click_2")
btn_3 = ttk.Button(app, text="Click_3")

btn_1.grid(row=1, column=0)
btn_2.grid(row=1, column=1)
btn_3.grid(row=1, column=2)

app.mainloop()