from tkinter import *

window = Tk()

#Creating Window
window.title("Hangman")
window.geometry("275x250")

#Creating Widgets
lblEnterLetter = Label(window, text="Enter Letter:")
txtEnterLetter = Entry(window)
btnGuessLetter = Button(window, text="Submit Letter")

#Packing
lblEnterLetter.grid(row = 1, column = 1)
txtEnterLetter.grid(row = 1, column = 2)
btnGuessLetter.grid(row = 1, column = 3)

window.mainloop()