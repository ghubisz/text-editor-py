from tkinter import *

#create root window
root = Tk()

#design
root.geometry("350x250")
root.minsize(height=560,
             width=560)
root.maxsize(height=250,
             width=350)
root.title("Text Editor")

#scrollbar implementation
scrollbar = Scrollbar(root)

scrollbar.pack(side=RIGHT,
               fill=Y)

text_info = Text(root,
                 yscrollcommand=scrollbar.set)
text_info.pack(fill=BOTH)

scrollbar.config(command=text_info.yview)

#widgets, buttons, etc
root.mainloop()