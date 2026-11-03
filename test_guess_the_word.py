# JC Gatela
# CIS256 Fall 2026
# Programming Assignment 4

from guess_the_word import (
    WORDS, select_word, process_guess, display_word
)


# Test that the selected word comes from our word list
def test_select_word():
    word = select_word()
    assert word in WORDS


# Test that the game recognizes a correct guess
def test_correct_guess():
    guessed_letters = []

    result = process_guess("apple", "a", guessed_letters)

    assert result == "correct"
    assert "a" in guessed_letters


# Test that the game recognizes an incorrect guess
def test_incorrect_guess():
    guessed_letters = []

    result = process_guess("apple", "z", guessed_letters)

    assert result == "incorrect"
    assert "z" in guessed_letters


# Test that repeated letters are revealed together
def test_repeated_letters():
    guessed_letters = []

    result = process_guess("apple", "p", guessed_letters)

    assert result == "correct"
    assert display_word("apple", guessed_letters) == "_ p p _ _"


# Test that guessing the same letter twice is recognized
def test_duplicate_guess():
    guessed_letters = ["a"]

    result = process_guess("apple", "a", guessed_letters)

    assert result == "already guessed"
    assert guessed_letters == ["a"]


# Test that unguessed letters remain hidden
def test_display_word():
    guessed_letters = ["a"]

    result = display_word("banana", guessed_letters)

    assert result == "_ a _ a _ a"
