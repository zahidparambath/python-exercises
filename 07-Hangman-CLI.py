# Exercise Name:
# 	07-Hangman-CLI
# Description:
# 	Create a hangman CLI game
# Rough game logic:
# 	1. Pick a random word. (Initially just use a hardcoded word like 'watermelon'. Random selection can be done later.)
# 	2. Initialize Guess Count to 6
# 	3. Show one underscore for each character in the word. For example, in case of 'watermelon', show 10 underscores like: _ _ _ _ _ _ _ _ _ _ 
# 	4. Prompt user to input their guess
# 		- Show a sorted list of already guessed characters
# 		- Guess should be ONE character from the alphabet
# 		- Guessed character should be new and not have been previously guessed
# 	5. Check if that character exists in the selected word
# 		a. If the character exists, reveal the character in its position. 
# 		   For example, in case of 'watermelon' and user guessed 'e', show: _ _ _ e _ _ e _ _ _
# 		b. If the character does not exist in the selected word, show warning and decrement Guess Count by one
# 	6. If the Guess Count
# 		a. is greater than zero, loop and take another input
# 		b. becomes zero before guessing all the characters in the word, Game Over.
# For improvement:
# 	https://random-word-api.herokuapp.com/word

import requests 

URL = 'https://random-word-api.herokuapp.com/word'
response = requests.get(URL)
word = response.json()[0]
guessCount = 6
wordLength = len(word)
resultWord = "_" * wordLength
guessList = []
print()
print("""--------------------Welcome to Hangman CLI Game--------------------
      
-- Application will randomly pick a word from the internet.
-- You are expected to guess one letter in the word at each turn.
-- The objective is to correctly guess the word that the application has picked
-- You can have upto six incorrect guesses (i.e guessed letter not in the word) before it's a game over.
-- You have 6 incorrect option to guess
Good Luck""")
print()
print("Ok here we go: The secret word is {} character long".format(wordLength))
print('\n')
while True :

    if len(guessList)==0:
        print("Secret word: {}".format(resultWord))
        print("So far you have guessed : Nothing")

    guessLetter = input("Enter your guess: ")
    guessList.append(guessLetter)
    print()
    if guessLetter in word :
        print(f"Yay! That was a good guess! The letter '{guessLetter}' exist in the secret word.")
        print('\n')

    else :
        print(f"Uh Oh That was not a great guess the letter '{guessLetter}' does not exist in the secret word.")
        guessCount-=1
        print(f"You have {guessCount} incorrect guess left.")
        print('\n')
    for index,char in enumerate(word):
        if char == guessLetter:
            wordList = list(resultWord)
            wordList[index] = char
            resultWord = ''.join(wordList)
            
    print(f"Secret word : {resultWord}")
    print(f"So far you have guessed : {guessList}")

    if(resultWord == word ):
        print()
        print(f"VICTORY!!!!! The Secret word is {resultWord}")
        print()
        break

    elif guessCount<1 :
        print()
        print(f"LOST!!!!! You are out of incorrect guesses, The Secret Word is : {word}")
        print()
        break
         