import tkinter as tk
from platform import python_version

def ChamaGrid ():
	def main(args):
		root = tk.Tk()

		lbl1= tk.Label(root, text="Texto superior", bg="red", fg="white")
		lbl2= tk.Label(root, text="Texto intermediário", bg="yellow", fg="black")
		lbl3= tk.Label(root, text="Texto inferior", bg="green", fg="white")

		lbl1.grid(row=0,column=0, padx= 10, pady=10)
		lbl2.grid(row=1,column=1,padx= 10, pady=10)
		lbl3.grid(row=2,column=2,padx= 10, pady=10)

		root.mainloop()
		return 0

	if __name__ == '__main__':
		print (python_version())   #somente para verificar que estamos no ambiente virtual python 3.5
		import sys
		sys.exit(main(sys.argv))