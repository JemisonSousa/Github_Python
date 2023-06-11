from tkinter import *
from tkinter import ttk 
from tkinter import filedialog
import sys, os

# pyinstaller --onefile -w --ico nome.ico Arquivo.py



# def pickaudiofile():
#     # FilePicker = Tk()
#     # FilePicker.withdraw()  # we don't want a full GUI, so keep the root window from appearing
#     # FilePicker.focus_force()
#     filename = filedialog.askopenfilename(filetypes = [('PNG files', '.png'), ('JPG files', '.jpg')])

#     # Assert file selected
#     if filename == "":
#         print("File select canceled.")
#         # sys.exit(0)

#     # FilePicker.destroy()  # Destory our TKinter instance

#     print(filename)
#     return filename

# class Principal:
    
#     def funcaoBtn(self):
#         self.conteudo.configure(text='O texto foi mudado pela função', background='red')
#         self.root.config(background='black')
    
#     def __init__(self):
#         self.root = Tk()
#         self.root.title("Sistema Qualker®")
#         self.root.geometry('600x400+5+300')
#         self.root.config(background='black')
#         # self.root.iconbitmap(default='VS_Code_GitHub\Imagens\_frutas\_botoes\_jpg_bar-graph.ico')
#         icon = PhotoImage(file="VS_Code_GitHub\Exemplos\_orange-icon.png")
#         self.root.iconphoto(True,icon)

#         frameA = LabelFrame(
#                             self.root,
#                             text="Escolhas",
#                             borderwidth=3,
#                             background='#C9C9C9',
#                             relief='ridge',
#                             cursor='sb_up_arrow',
#                             padx=1, pady=1,
#                             width=0, height=0 #não responde, apeas mexendo no frame
#                             )
#         frameA.pack(side='left', fill=BOTH, expand=False)

#         labelA = Label(
#                        frameA,
#                        text="lado esquerdo",
#                        padx=1, pady=1,
#                        width=20, height=2
#                        )
#         labelA.pack()

#         frameB = LabelFrame(
#                             self.root,
#                             text="Detalhes",
#                             relief='sunken'
#                             )
#         frameB.pack(side='right', fill=BOTH, expand=True)

#         btn_clique = ttk.Button(
#                             frameB,
#                             text="Mudar a cor do fundo",
#                             command=self.funcaoBtn,
#                             )
#         btn_clique.pack(pady=5, side=BOTTOM)
        
#         btn_open = ttk.Button(
#                             frameB,
#                             text="Open",
#                             command=pickaudiofile
#                             )
#         btn_open.pack(pady=5, side=BOTTOM)

#         self.conteudo = Label(
#                             frameB,
#                             text='Texto a ser mudado'
#                             )
#         self.conteudo.pack(pady=30)

#         self.root.update
#         self.root.mainloop()

# Principal()










root = Tk()
root.winfo_toplevel()
root.withdraw()

filePath = filedialog.askopenfilename(initialdir="~/", title="Select file")

root.update()

fileSize = os.path.getsize(filePath)
print("File selected: " + filePath)
print("\nfile is: " + str(fileSize) + " bytes\n")

#.............................................................



# root.deiconify()
# button1 = (root, text="SHA256", command=SHA256(filePath))
# button1.pack()

# fileType = input("specify checksum type: " + "(ex. md5, sha1, sha256)" + "\n")

# if fileType.lower() == "md5":
#     message = MD5(filePath)
#     print("MD5:\n" + message + "\n")
# elif fileType.lower() == "sha256":
#     message = SHA256(filePath)
#     print("SHA256:\n" + message + "\n")
# elif fileType.lower() == "sha1":
#     message = SHA1(filePath)
#     print("SHA1:\n" + message + "\n")

# elif fileType.lower() not in hashTypes:
#     print("Invalid file type \n\n")