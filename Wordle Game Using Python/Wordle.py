import random
import tkinter as tk
from tkinter import messagebox

class WordleApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Wordle Game")
        
        self.word_to_guess = self.choose_word()
        self.guessed_letters = []
        self.max_attempts = 6
        self.attempts = 0

        self.create_widgets()

    def choose_word(self):
        words = ["python", "guitar", "elephant", "programming", "challenge", "computer"]
        return random.choice(words)

    def display_word(self):
        display = ""
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        return display

    def create_widgets(self):
        self.label = tk.Label(self.master, text=self.display_word(), font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master, font=("Helvetica", 14))
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess)
        self.guess_button.pack()

    def make_guess(self):
        guess = self.entry.get().lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in self.guessed_letters:
                messagebox.showinfo("Invalid Guess", "You already guessed that letter. Try again.")
            elif guess in self.word_to_guess:
                self.guessed_letters.append(guess)
                self.label.config(text=self.display_word())
                if self.display_word() == self.word_to_guess:
                    messagebox.showinfo("Congratulations!", "You guessed the word!")
                    self.reset_game()
            else:
                self.attempts += 1
                messagebox.showinfo("Wrong Guess", f"Wrong guess! {self.max_attempts - self.attempts} attempts remaining.")
                if self.attempts == self.max_attempts:
                    messagebox.showinfo("Game Over", f"Sorry, you ran out of attempts. The word was {self.word_to_guess}.")
                    self.reset_game()
        else:
            messagebox.showinfo("Invalid Input", "Please enter a single letter.")

        self.entry.delete(0, tk.END)

    def reset_game(self):
        self.word_to_guess = self.choose_word()
        self.guessed_letters = []
        self.attempts = 0
        self.label.config(text=self.display_word())

if __name__ == "__main__":
    root = tk.Tk()
    app = WordleApp(root)
    root.mainloop()
