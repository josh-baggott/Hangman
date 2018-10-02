from tkinter import *

window = Tk()

#Creating Window
window.title("Hangman")
window.geometry("300x300")

#Creating Widgets
lblEnterLetter = Label(window, text="Enter Letter:")
txtEnterLetter = Entry(window)
btnGuessLetter = Button(window, text="Submit Letter")

#Packing
lblEnterLetter.pack()
txtEnterLetter.pack()
btnGuessLetter.pack()

window.mainloop()