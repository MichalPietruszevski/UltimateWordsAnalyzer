import re
import tkinter as tk
from PIL import ImageTk, Image

def count_bible(pattern):
  occurence = 0
  with open ('static/ACV.txt', 'r') as bible:
    bible = bible.read()
    matches = re.compile(pattern).finditer(bible)
    for match in matches:
      occurence += 1
  return occurence

def click_to_count():
    word = word_zone.get()
    number_of_occurence=count_bible(word)
    L2.config(text=str(number_of_occurence))

root = tk.Tk()
root.title('Bible words counting')
root.geometry('700x650')
root.iconbitmap('static/open-book.ico')

img = ImageTk.PhotoImage(Image.open('static/bible.jpg'))

Left_side = tk.Label(root, image=img)
Left_side.grid(column=0,row=1,rowspan=2)

Right_side = tk.Label(root, image=img)
Right_side.grid(column=3,row=1,rowspan=2)

L1 = tk.Label(root, text='Enter word in blank field, bless!',font=('Arial',20))
L1.config(anchor='center')
L1.grid(column=0,row=0,columnspan=3)

L2 = tk.Label(root, text='',
                  padx=2,pady=2,font=('Arial',44))
L2.grid(column=1,row=2)

word_zone = tk.Entry(root,bd=5)
word_zone.grid(column=1,row=1)


B1 = tk.Button(root,text='search', command=click_to_count)
B1.grid(column=2,row=1)

root.mainloop()
