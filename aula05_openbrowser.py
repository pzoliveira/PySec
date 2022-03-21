import webbrowser
from tkinter import *

def google():
    webbrowser.open('www.google.com.br')


if __name__ == '__main__':
    root = Tk( )
    root.title("Open Browser")
    root.geometry('300x200')
    mygoogle = Button(root, text='Open the Google site', command=google).pack(pady=20)
    root.mainloop()
