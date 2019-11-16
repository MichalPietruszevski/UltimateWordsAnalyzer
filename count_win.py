import tkinter as tk
import re
from tkinter import filedialog





#Create window for choosing directory to txt file and counting word frequency in that.
class Count_app:
	#Set initial options
	def __init__(self, master):
		self.master = master
		self.master.title("Ultimate Words Analyzer 01.00 - Word's frequency")
		self.master.geometry("400x200")
		self.master.iconbitmap('static/open-book.ico')
		#self.master.filename = filedialog.askopenfilename(initialdir='books/', title='Select a file', filetypes=(('txt files','*.txt'),('all files','*.*')))

		self.frame = tk.Frame(self.master)

		#Creat info lable
		self.text_for_info  = "Choose directory for right .txt file\n and enter your word to counting."
		self.info_menu = tk.Label(self.frame, text = self.text_for_info)

		self.direc = tk.Button(self.frame, text = 'Search for text', command = self.loc_of_file)

		self.show_directory = tk.Label(self.frame, text = '')

		self.word_field = tk.Entry(self.frame,bd = 5, width=30)

		self.word_count_butt = tk.Button(self.frame, text='Enter your word', command = self.click_to_count)

		self.display_number = tk.Label(self.frame,  text='', font=('Ariel', 30))

		self.info_menu.pack()
		self.direc.pack()
		self.show_directory.pack()
		self.word_field.pack()
		self.word_count_butt.pack()
		self.display_number.pack()
		self.frame.pack()

	def loc_of_file(self):
		self.master.filename = filedialog.askopenfilename(initialdir='books/',
				title='Select a file', filetypes=(('txt files','*.txt'),('all files','*.*')))
		self.show_directory.config(text = self.master.filename)

	def count_words(self,pattern, path_to_book):
		self.occurence = 0
		self.path_to_book = path_to_book
		with open (self.path_to_book, 'r') as book:
			self.book = book.read()
			self.matches = re.compile(pattern).finditer(self.book)
			for match in self.matches:
				self.occurence += 1
		return self.occurence

	def click_to_count(self):
		try:
			self.pattern = self.word_field.get()
			self.number_of_occurence= self.count_words(self.pattern, self.master.filename)
			self.display_number.config(text=str(self.number_of_occurence))
		except AttributeError:
			self.text_of_empty_dir_error = "Choose directory first"
			self.display_number.config(font = ('Arial',12), text= self.text_of_empty_dir_error)
