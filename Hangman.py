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

choice = randint(0, 49)
compWord = states[choice]
blanks = []
falseInput = []
for letters in compWord:
    blanks += "_"

def checkGuess(userInput):
    lowerWord = compWord.lower()
    lowerInput = userInput.lower()
    if userInput.isalpha() and len(userInput) == 1:
        if lowerInput in lowerWord:
            for letter in lowerWord:
                if letter == lowerInput:
                    blanks[] = lowerInput
        else:
            falseInput.append(lowerInput)
            failedStr = ' '.join(falseInput)
            print("You have tried: " + failedStr)


while blanks != compWord:
    userInput = input("Input a letter: ")
    checkGuess(userInput)
    if blanks[0] != "_":
        blanks[0] = blanks[0].upper()
    print(blanks)

print('You did it! The word was: ' + compWord)