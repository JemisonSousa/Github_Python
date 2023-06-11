from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("700x400")

image=Image.open("Imagens\_frutas\pear-icon.png")
img=image.resize((50, 50))
my_img=ImageTk.PhotoImage(img)
label=Label(root, image=my_img)
label.pack(side=LEFT)

image2=Image.open("Imagens\_frutas\pear-icon.png")
img2=image2.resize((100, 100))
my_img2=ImageTk.PhotoImage(img2)
label2=Label(root, image=my_img2)
label2.pack(side=LEFT)

image3=Image.open("Imagens\_frutas\pear-icon.png")
img3=image3.resize((200, 200))
my_img3=ImageTk.PhotoImage(img3)
label3=Label(root, image=my_img3)
label3.pack(side=RIGHT)

root.mainloop()