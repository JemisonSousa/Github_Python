from tkinter import *

root = Tk()
root.title("test window")
root.geometry('400x220+500+250')
root.configure(background="dark gray")


def submit(*args):
    root.iconify()
    popup_root_window = Toplevel()
    popup_root_window.geometry('300x50+550+300')
    popup_root_window.resizable(width=False, height=False)
    popup_root_window.focus_force()
    popup_root_window.grab_set()
    popup_root_window_label = Label(popup_root_window, text="new window open successfully.")
    popup_root_window_label.pack(anchor=CENTER, padx=10, pady=20)


frame = Frame(root, bd=4, relief="raise", height=100, width=250)
frame.pack(fill="both", padx=70, pady=35)
frame.pack_propagate(0)

submit_button = Button(frame, text="Submit", command=submit, width=10)
submit_button.grid(row=0, column=0)

cancel_button = Button(frame, text="Cancel", width=10, command=root.quit)
cancel_button.grid(row=0, column=1)

root.mainloop()
