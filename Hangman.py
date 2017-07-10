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
    if userInput == compWord or userInput == lowerWord:
        i = 0
        for letters in compWord:
            blanks[i] = letters
            i += 1
        print(blanks)
    else:
        if " " in lowerWord:
            blanks[lowerWord.index(" ")] = " "
        if userInput.isalpha() and len(userInput) == 1:
            if lowerInput not in lowerWord:
                falseInput.append(lowerInput)
                failedStr = ' '.join(falseInput)
                print("You have tried: " + failedStr)
            else:
                list(lowerWord)
                for i, letter in enumerate(lowerWord):
                    if letter == " ":
                        blanks[i] == " "
                    elif letter == lowerInput:
                        blanks[i] = lowerInput

while ''.join(blanks) != compWord:
    print(blanks)
    userInput = input("Input a letter: ")
    checkGuess(userInput)
    blanks[0] = blanks[0].title()
    if " " in compWord:
        location = compWord.index(" ")
        blanks[location + 1] = blanks[location + 1].title()


print('You did it! The word was: ' + compWord)