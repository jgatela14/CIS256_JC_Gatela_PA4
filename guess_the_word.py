# JC Gatela
# CIS256 Fall 2026
# Programming Assignment 4

import random

# List of words the game can randomly choose from
WORDS = ["apple", "banana", "orange", "grape", "cherry"]


# Select a random word from the list
def select_word():
    return random.choice(WORDS)


# Display the word with unguessed letters hidden
def display_word(word, guessed_letters):
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    return display.strip()


# Start the game
def main():
    word = select_word()
    guessed_letters = []

    print("Welcome to Guess the Word!")
    print("Word:", display_word(word, guessed_letters))


if __name__ == "__main__":
    main()
