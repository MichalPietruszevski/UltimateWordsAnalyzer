import tkinter as tk
from count_win import Count_app
from words_cloud_win import Word_cloud_app

#Create menu main window for three operactions: word's frequency, word cloud, word compreing between texts
class Menu:
	#Set initial three buttons which redirecting to specify windows
	def __init__(self, master):
		self.master = master
		self.master.title('Ultimate Word Analyzer 01.00')
		self.master.geometry("400x200")
		self.master.iconbitmap('static/open-book.ico')

		self.frame = tk.Frame(self.master)

		#Creat info lable
		self.text_for_info  = "Hello! This proram allows you to make three diffrent operations:\n counting word frequency in text,\n making a word-cloud,\n comper word's frequency between diffrent text."
		self.info_menu = tk.Label(self.frame, text = self.text_for_info)

		#Creat three buttons
		self.button_for_count = tk.Button(self.frame, text = "Count word's frequency", width = 25, command = self.count_window)
		self.button_for_cloud = tk.Button(self.frame, text = "Create word cloud", width = 22, command = self.cloud_window)
		self.buttom_for_compare = tk.Button(self.frame, text = "Compere word's frequency in more texts", width = 32, command = '')


		#Set posiotion of the info_menu
		self.info_menu.pack()

		#Set position of the buttons
		self.button_for_count.pack()
		self.button_for_cloud.pack()
		self.buttom_for_compare.pack()

		#Set position of the frame
		self.frame.pack()

	def count_window(self):
		self.hide()
		self.new_count_window = tk.Toplevel(self.master)
		self.app_count = Count_app(self.new_count_window)

	def cloud_window(self):
		self.hide()
		self.new_cloud_window = tk.Toplevel(self.master)
		self.app_cloud = Word_cloud_app(self.new_cloud_window)


	def hide(self):
		self.master.withdraw()

def main():
	root = tk.Tk()
	app = Menu(root)
	root.mainloop()

if __name__  == '__main__':
	main()
