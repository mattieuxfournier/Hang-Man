import random
import sys
import os
import pyfiglet

stages = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========
    """,
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
    """,
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
    """,
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
    """,
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
    """,
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
    """,
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
    """
]

def clear_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix-based systems (Linux, macOS)
        os.system('clear')

def random_word():
    clear_terminal()
    with open('words_cleaned.txt') as dictionary:
        WORDS = dictionary.read().split()
        pick = random.randint(1, len(WORDS)-1)
        word = WORDS[pick].lower()
        pick_hidden = ' '.join('_'*len(word))
        hang_man(0, word, pick_hidden, set())

def hang_man(guess_left, word, pick_hidden, guessed_letters):
    while not isWon(word, guess_left, pick_hidden):  
        print(stages[guess_left])
        print(f'You have {pick_hidden.count("_")} letters left to guess')
        print(pick_hidden)
        print(f"Guessed letters: \n{', '.join(sorted(guessed_letters))}")
        guess = input('What will you guess?: ').strip().lower()
        clear_terminal()
        if guess in ("quit", "exit"):
            print("Thanks for playing! Goodbye!")
            sys.exit()
        if not guess.isalpha():
            print("Please enter a valid letter or word.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        guessed_letters.add(guess)
        pick_hidden, guess_left = isInOrNot(guess_left, guess, word, pick_hidden)
    while isWon(word, guess_left, pick_hidden):
        play_again = input('Would you like to play again? Y/N: ').upper()
        if play_again == 'Y':
            return random_word()
        if play_again == 'N':
            print('See you next time!')
            sys.exit()
        else:
            print('Sorry that is an invalid input')
            
def isWon(word, guess_left, pick_hidden):
    if guess_left >= 6:
        clear_terminal()
        print(stages[6])
        print(pick_hidden)
        print(f"The word was: {word}")
        print('You lost!')
        return True
    if pick_hidden.count('_') == 0:
        clear_terminal()
        print(stages[guess_left])
        print(word)
        print('You won!')
        return True
    return False

def isInOrNot(guess_left, guess, word, pick_hidden):
    guess_lst = list(guess)
    word_lst = list(word)
    char_hidden = list(pick_hidden.replace(" ", ""))
    correct_guess = False
    if len(guess_lst) == 1:
        for i in range(len(guess_lst)):
            for j in range(len(word_lst)):
                if guess_lst[i] == word_lst[j]:
                    char_hidden[j] = guess_lst[i]
                    correct_guess = True
        if not correct_guess:
            guess_left += 1
    elif len(guess_lst) > 1:
        if guess != word:
            guess_left += 1
        else:
            char_hidden = list(word)

    updated_pick_hidden = ' '.join(char_hidden)
    return updated_pick_hidden, guess_left

def welcome_message():
    print(pyfiglet.figlet_format('Welcome to hang man!', justify = 'center'))
    print('Your goal is to guess letters or words to discover the hidden word')
    while True:
        choice = input('Would you like to play? Y/N: ').strip().upper()
        if choice == 'Y':
            clear_terminal()
            return random_word()
        elif choice == 'N':
            print('Farewell!')
            sys.exit()
        else:
            print('Sorry! That is an invalid choice!')

welcome_message()