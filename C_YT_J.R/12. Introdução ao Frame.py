from logging import root
from tkinter import *

root = Tk()
root.title("Frame")
# root.geometry("300x300")

frame_login = Frame(root)

label_usuario = Label(frame_login, text="Usuário:")
label_password = Label(frame_login, text="Password:")
label_password = Label(frame_login, text="Password:")
text_usuario = Entry(frame_login)
text_password = Entry(frame_login)
cmd_entrar = Button(frame_login, text="Entrar")

frame_login.grid()
label_usuario.grid(row=0, column=0)
text_usuario.grid(row=0, column=1)
label_password.grid(row=1, column=0)
text_password.grid(row=1, column=1)
cmd_entrar.grid(row=2, column=0, columnspan=2)


root.mainloop()