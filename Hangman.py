from random import randint
from string import ascii_lowercase

class Hangman():
    def __init__(self):
        self.word = self.get_word()
        self.letter_row = '*' * len(self.word)
        self.letters_guessed = []
        self.guesses_left = 8
    
    def get_letter_row(self):
        return self.letter_row

    def get_guesses_left():
        return guesses_left

    def get_word(self):
        return "apple"

    def guess_letter(self, letter):
        if type(letter) != str and len(letter) != 1 and letter not in ascii_lowercase:
            raise TypeError("Value given is not a letter")
        if letter in self.letters_guessed:
            raise ValueError("Letter has already been guessed")
        elif letter in self.word:
            pass
        else:
            pass
        
    def check_win(self):
        return False
        


if __name__ == "__main__":
    this_game = Hangman()
    
    while not this_game.check_win():
        print(this_game.get_letter_row())
        user_guess = input("Guess a letter:\t")
        this_game.guess_letter(user_guess)
        print("Guesses Left:\t", this_game.guesses_left)
    
    print(this_game.check_win())