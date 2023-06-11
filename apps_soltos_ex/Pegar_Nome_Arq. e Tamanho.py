from tkinter import *
from tkinter import ttk 
from tkinter import filedialog
import sys, os


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