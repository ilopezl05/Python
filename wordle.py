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
    tries = 0

    while rightWord != True:

        if tries <= 5:
            # FYI to warn the user of final opportunity
            if tries == 5:
                print('\n--------This is your last chance, make it count.--------')

            # Get try word from user
            tryWord = input('\nEnter your word: ')
            # Check if try word is 5 characters long
            while len(tryWord) != 5:
                print('--------Make sure you are entering a 5 letter word.--------')
                tryWord = input('\nEnter your word: ')

            # Increase tries by one very time a word is submitted
            tries += 1

            # Find letters in right place
            for tryLetter, guessLetter in zip(tryWord, wordToGuess):
                if tryLetter == guessLetter:
                    print('"{}" is in the right place.'.format(tryLetter))
                else:
                    # Find letters not in right place
                    if tryLetter in wordToGuess:
                        print('"{}" is NOT in the right place.'.format(tryLetter))
                    else:
                        # Add character to list of letters not in the word to be guessed
                        if tryLetter not in lettersNotInWord:
                            lettersNotInWord.append(tryLetter)

            print('\nIncorrect letters:')
            lettersNotInWord.sort()
            print(lettersNotInWord)

            # check if user guessed the word
            if tryWord == wordToGuess:
                print('\n--------Good job, the word was {}--------'.format(wordToGuess))
                rightWord, tries, lettersNotInWord, wordToGuess = continuePlaying(rightWord, tries, lettersNotInWord, words)

        else:
            print("\n--------Good game, you'll get it next time.--------")
            rightWord, tries, lettersNotInWord, wordToGuess = continuePlaying(rightWord, tries, lettersNotInWord, words)

def getWord(list):
    randNum = random.randrange(0, len(list))
    return list[randNum]

def continuePlaying(breaker, counter, letterList, words):
    keepPlaying = input('\nDo you want to continue playing (y for yes, anything else for no)? ')
    if keepPlaying == 'Y' or keepPlaying == 'y':
        word = getWord(words)
        breaker = False
        counter = 0
        letterList = []
        return breaker, counter, letterList, word
    else:
        print('\nSee you around.')
        breaker = True
        return breaker, counter,letterList, words

if __name__ == '__main__':
    main()