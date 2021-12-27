from tkinter import *

from tkinter.font import BOLD

from tkinter import messagebox


class App:
	"""GUI class for App"""
	def __init__(self, parent):

		super(App, self).__init__()

		self.parent = parent
		

		# labels config dict
		self.lbl_config = {
			"relief": RIDGE,
			"font":   ("Verdana", 16)
		}

		# entry config dict
		self.entry_config = {
			"length": 15,
			"ipady": 10
		}
			#Validate

		self.create_widgets()
		# self.trace()
		

	def create_widgets(self):

		"""Create GUI widgets"""

		self.cmd_lbl = Label(self.parent, text="Enter Phone: ",foreground="black",font=("bold",15))

		self.cmd_lbl.configure(background="black")

		self.cmd_lbl.grid(row=3, column=2)

		self.cmd_lbl.place(x=40,y=105)

		self.cmd_lbl.configure(background="#2fa4e7")

		#todo
		# create entry for command
		self.str_var = StringVar()
		
		self.cmd_entr = Entry(self.parent,textvariable=self.str_var)

		self.cmd_entr.grid(row=3, column=3)

		self.cmd_entr.place(x=160,y=105,width=210,height=45)

		self.cmd_entr.configure(background="#2fa4e7")

		# create response label

		# create a button 
		self.cmd_btn = Button (self.parent,text="Trace",background="#00030a",foreground="#2fa4e7",width=17,font=(16),activebackground="#00030a",activeforeground="#2fa4e7")
		self.cmd_btn.place(x=380,y=105,height=45)
		# make it not resizable
		#


	def widget_pack(self):
		"""Pack widgets"""
		pass
		

if __name__ == '__main__':

	root = Tk()

	root.geometry("600x500")

	root.title("Phone Tracker")

	root.configure(background="#2fa4e7")
	# add resizable false option here	

	root.resizable(False,False)

	app = App(root)

	root.mainloop()
