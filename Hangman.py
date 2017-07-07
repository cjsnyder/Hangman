"""Created: 7/7/2017 ~ By; Conner Snyder
Purpose: Basic hangman game
Use: Learning and test of knowledge"""

from random import randint


states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
          'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
          'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
          'Maine' 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
          'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
          'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
          'North Carolina', 'North Dakota', 'Ohio',
          'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
          'South  Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',
          'Vermont', 'Virginia', 'Washington', 'West Virginia',
          'Wisconsin', 'Wyoming']
choice = randint(0, 50)
compWord = states[choice]
blanks = []
for letters in compWord:
    blanks += "_"

def checkGuess(userInput):
    if userInput.isalpha():
        if userInput in compWord:
            blanks[compWord.index(userInput)] = userInput

while blanks != compWord:
    userInput = input("Input you letter: ")
    checkGuess(userInput)
    print(blanks)