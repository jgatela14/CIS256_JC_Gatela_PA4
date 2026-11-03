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


# Check whether the player's guess is correct
def process_guess(word, guess, guessed_letters):
    if guess in guessed_letters:
        return "already guessed"

    guessed_letters.append(guess)

    if guess in word:
        return "correct"
    else:
        return "incorrect"


# Run the word guessing game
def main():
    word = select_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Guess the Word!")
    print("You have 6 incorrect guesses.")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))

        guess = input("Guess a letter: ").lower().strip()

        # Make sure the player enters only one letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        result = process_guess(word, guess, guessed_letters)

        if result == "already guessed":
            print("You already guessed that letter.")
            continue
        elif result == "correct":
            print("Correct!")
        else:
            attempts -= 1
            print("Incorrect!")
            print("Attempts remaining:", attempts)

        # Check whether every letter has been guessed
        if all(letter in guessed_letters for letter in word):
            print("\nWord:", display_word(word, guessed_letters))
            print("Congratulations! You guessed the word!")
            break

    else:
        print("\nGame over! The word was:", word)

if __name__ == "__main__":
    main()
