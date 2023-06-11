from tkinter import filedialog
import sys

def pickaudiofile():
    # FilePicker = Tk()
    # FilePicker.withdraw()  # we don't want a full GUI, so keep the root window from appearing
    # FilePicker.focus_force()
    filename = filedialog.askopenfilename(filetypes = [('PNG files', '.png'), ('JPG files', '.jpg')])

    # Assert file selected
    if filename == "":
        print("File select canceled.")
        sys.exit(0)

    # FilePicker.destroy()  # Destory our TKinter instance

    print(filename)
    return filename



pickaudiofile()