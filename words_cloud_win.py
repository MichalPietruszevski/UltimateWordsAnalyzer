import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from wordcloud import WordCloud, STOPWORDS

class Word_cloud_app:
    #Set initial operactions
    def __init__(self, master):
        self.master = master
        self.master.title("Ultimate Words Analyzer 01.00 - Word's Cloud Generator")
        self.master.geometry("400x200")
        self.master.iconbitmap('static/open-book.ico')

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.loc_file = tk.Button(self.frame, text='Search for file', command=self.loc_of_file)
        self.loc_file.pack()

        self.show_directory = tk.Label(self.frame
                                       ,text='')
        self.show_directory.pack()

        self.butt_for_cloud = tk.Button(self.frame, text='Generate WordCloud',command=self.word_cloud)
        self.butt_for_cloud.pack()

    def loc_of_file(self):
        self.master.filename = tk.filedialog.askopenfilename(initialdir='books/',
                                                          title='Select a file',
                                                          filetypes=(('txt files', '*.txt'), ('all files', '*.*')))
        self.show_directory.config(text=self.master.filename)

    def word_cloud(self):
        try:
            self.path_to_book = self.master.filename
            with open(self.path_to_book,'r') as book:
                text = book.read()
                stopwords = set(STOPWORDS)
                mask = np.array(Image.open('static/book.jpg'))
                cloud = WordCloud(stopwords=stopwords, max_words=200, mask=mask, background_color="white").generate(text)
                plt.imshow(cloud, interpolation='bilinear')
                plt.axis('off')
                plt.show()
        except AttributeError:
            self.text_of_error = 'At first choose file'
            self.show_directory.config(font=('Arial',12), text=self.text_of_error)

