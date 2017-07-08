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
          'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',
          'Vermont', 'Virginia', 'Washington', 'West Virginia',
          'Wisconsin', 'Wyoming']

choice = randint(0, 50)
compWord = states[choice]
blanks = []
falseInput = []
for letters in compWord:
    blanks += "_"

def checkGuess(userInput):
    if userInput.isalpha():
        try:
            if compWord.index(userInput) != -1:
                blanks[compWord.index(userInput)] = userInput
        except ValueError:
            falseInput.append(userInput)
            failedStr = ' '.join(falseInput)
            print("You have tried: " + failedStr)

while blanks != compWord:
    userInput = input("Input a letter: ")
    checkGuess(userInput)
    print(blanks)

print('You did it! The word was: ' + compWord)