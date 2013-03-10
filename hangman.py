import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    return 0 not in [c in ''.join(lettersGuessed) for c in secretWord]



def getGuessedWord(secretWord, lettersGuessed):
    res = ''
    for c in secretWord:
      if c not in ''.join(lettersGuessed):
        res += "_ "
      else:
        res +=  c
    return res

def getAvailableLetters(lettersGuessed):
    res = ''
    for c in string.ascii_lowercase:
        if c not in ''.join(lettersGuessed):
          res += c
    return res


def hangman(secretWord):
    print "Welcome to the game, Hangman!\nI am thinking of a word that is " + str(len(secretWord)) + " letters long"
    def checker(word, guessed, guesses, guess_list):
      if guesses > 0:
        if isWordGuessed(word, guessed):
          print "-----------\nCongratulations, you won!"
        else:
          print "-------------\nYou have " + str(guesses) + " guesses left.\nAvailable letters: " + getAvailableLetters(guessed) + " "
          guess = raw_input("Please guess a letter:").lower()

          guessed = list_append(guessed, guess)
          if not guess in guess_list:
            if guess not in word:
              print "Oops! That letter is not in my word " + getGuessedWord(secretWord, guessed)
              return checker(word, list_append(guessed, guess), guesses - 1, guess_list + guess)
            else:
              print "Good guess: " + getGuessedWord(secretWord, guessed)
              return checker(secretWord, list_append(guessed, guess), guesses, guess_list + guess)
          else:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, guessed)
            return checker(secretWord, list_append(guessed, guess), guesses, guess_list)
      else:
        print "-----------\nSorry, you ran out of guesses. The word was " + secretWord + "."

    checker(secretWord, [], 8, '')

def list_append(lst, item):
  lst.append(item)
  return lst

#Implementation
wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
