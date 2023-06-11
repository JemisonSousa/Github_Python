'''import tkinter.filedialog
     
tkinter.filedialog.asksaveasfilename()
tkinter.filedialog.asksaveasfile()
tkinter.filedialog.askopenfilename()
tkinter.filedialog.askopenfile()
tkinter.filedialog.askdirectory()
tkinter.filedialog.askopenfilenames()
tkinter.filedialog.askopenfiles()'''

import tkinter as tk
from tkinter import filedialog as fd 

def callback():
    name= fd.askopenfilename() 
    print(name)
    
errmsg = 'Error!'
tk.Button(text='Click to Open File', 
       command=callback).pack(fill=tk.X)
tk.mainloop()

