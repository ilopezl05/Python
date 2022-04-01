import random

print("""
 ------------------------------------------------------------------
|                         WORDLE-ISH                               |
 ------------------------------------------------------------------
""")

print("""Instructions:
You will have six chances to guess the five-letter word.
Every time you try to guess the word, the program will give you 
hints on what letters are in the word to be guessed based on the 
word you entered. It will also let you know if any of the letters 
are in the right place in the word you have to guess. The program 
will kepp track of the letters used that are not in the word to be 
guessed.
""")

def main():
    # List of words
    words = ["beach", "anger", "crowd", "draft", "enemy", "frame",
             "guide", "horse", "index", "judge", "knife", "limit",
             "motor", "nurse", "owner", "phase", "rugby", "share",
             "trial", "unity", "voice", "while", "youth"]
    # Get word from list
    wordToGuess = getWord(words)

    lettersNotInWord = []
    rightWord = False

    while rightWord != True:
        # Get try word from user
        tryWord = input('\nEnter your word: ')
        # Check if try word is 5 characters long
        while len(tryWord) != 5:
            print('Make sure you are entering a 5 letter word.')
            tryWord = input('\nEnter your word: ')

        # Find letters in right place
        for tryLetter, guessLetter in zip(tryWord, wordToGuess):
            if tryLetter == guessLetter:
                print('"{}" is in the right place.'.format(tryLetter))
            else:
                # Find letters not in right place
                if tryLetter in wordToGuess:
                    print('"{}" is in the word, but not in the right place.'.format(tryLetter))
                else:
                    # Add character to list of letters not in the word to be guessed
                    if tryLetter not in lettersNotInWord:
                        lettersNotInWord.append(tryLetter)

        print('\nIncorrect letters:')
        print(lettersNotInWord)

        # check if user guessed the word
        if tryWord == wordToGuess:
            print('Good job, the word was {}'.format(wordToGuess))
            keepPlaying = input('\nDo you want to continue playing (y for yes, anything else for no)? ')

            if keepPlaying == 'Y' or keepPlaying == 'y':
                main()
            else:
                print('\nSee you around.')

            rightWord = True

def getWord(list):
    randNum = random.randrange(0, len(list))
    return list[randNum]

if __name__ == '__main__':
    main()