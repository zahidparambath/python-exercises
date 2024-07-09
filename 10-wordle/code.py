# Exercise Name:
# 	10-wordle
# Description:
# 	Create the wordle game
# Resources:
# 	Valid Words List: https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93


import random

def read_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

file_path = 'valid-wordle-words.txt'
words = read_words(file_path)

RESET = "\033[0m"
GRAY_BG = "\033[100m"
YELLOW_BG = "\033[103m"
GREEN_BG = "\033[102m"

def guess_check(word, guess):
    result = ""
    for i in range(len(guess)):
        if guess[i] == word[i]:
            result += f"{GREEN_BG}{guess[i]}{RESET}"
        elif guess[i] in word:
            result += f"{YELLOW_BG}{guess[i]}{RESET}"
        else:
            result += f"{GRAY_BG}{guess[i]}{RESET}"
    return result

def wordle():
    word_to_guess = random.choice(words)
    attempts_left = 6

    print(f"*******{GREEN_BG}WELCOME{RESET} {YELLOW_BG}TO{RESET} {GREEN_BG}WORDLE{RESET}*******")
    print("Guess the 5 letter word. You have 6 attempts.")

    for attempt in range(attempts_left):
        guess = input(f"Attempt {attempt+1}/{attempts_left}: ").lower()

        if len(guess) != 5:
            print("Please enter a valid 5 letter word")
            continue

        if guess == word_to_guess:
            print(f"{GREEN_BG}{guess}{RESET}")
            print(f"Congratulations!!! You have guessed the word '{word_to_guess} correctly!!!'")
            break

        else:
            word_check = guess_check(word_to_guess, guess)
            print(word_check)

    else:
        print(f"Sorry, you've run out of attempts. The word was '{word_to_guess}'.")

wordle()
