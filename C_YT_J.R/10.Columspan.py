from tkinter import *

app = Tk()
app.title("GRID")
# app.geometry("500x500")
# app.geometry("%dx%d+%d+%d" % (500, 300, ((app.winfo_screenwidth())/2 - 500/2), ((app.winfo_screenheight())/2 - 300/2)))
app.iconbitmap("Ico-Fig-doc\carOfic.ico")

Label (app, text="Texto", width=21, bg="red").grid(column=0)
Label (app, text="Texto", width=21, bg="green").grid(column=1)
Label (app, text="Texto", width=21, bg="green").grid(column=2)
Label (app, text="Texto", width=21, bg="blue").grid(columnspan=3, sticky="we")
    

app.mainloop()