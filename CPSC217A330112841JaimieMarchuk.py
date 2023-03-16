# name: Jaimie Marchuk
# grace days used:0

import random
import sys
import termcolor

#Creating our class to begin our Wordle Game (aka the beginning of my stupendous code).
class Wordle:
    #Setting this class variable to an empty string (which will be updated later).
    currentWord = []
    #Setting this class variable to 0 (as it will be updated later in the code).
    numberOfUserGuesses = 0
    #Creating instance variables so we can take in our numberOfGuesses and file arguments into our class.
    def __init__(self, numOfGuesses, file):
        self.numOfGuesses = numOfGuesses
        self.file = file
    #Creating a class method that will read the Words.txt file line for line and create a list of all words present in that file.
    def readFile(self):
        #Creating instance variable with empty string (which words will be added to).
        self.listOWordsFromFile = []
        #Opening and reading Words.txt file.
        fileHandler = open((self.file), "r")
        #Creating a loop with the readlines function to read the file line by line.
        convertingLineToElement = fileHandler.readlines()
        for line in convertingLineToElement:
            #Appending the lines read into the instance variable to create a list of all the words in Words.txt.
            (self.listOWordsFromFile).append(line)
        #Safely closing file that was being read.
        fileHandler.close()

    # Creating a class method that will select a random word from the list of words created (listOWordsFromFile).
    def selectRandomWord(self):
        randomWord = random.choice(self.listOWordsFromFile)
        #Updating the Wordle word to be the random word selected.
        Wordle.currentWord = randomWord
    # Creating a class method that will take off the \n character from the end of the randomly selected word.
    def removeNewLineFromWord(self):
        Wordle.currentWord = (Wordle.currentWord).rstrip()
        #print(Wordle.currentWord)
        print(len(Wordle.currentWord))
    # Creating a class method to construct the game of Wordle.
    def playWordle(self):
        numberOfUserGuesses = Wordle.numberOfUserGuesses
        numberOfGuessesAllowed = self.numOfGuesses
        #Creating while loop that continues to loop whilst the number of user guesses is less than number of user guesses allowed.
        while numberOfUserGuesses < numberOfGuessesAllowed:
            #Updating numberofUserGuesses by one everytime the loop is ran.
            numberOfUserGuesses+=1
            currentWord = Wordle.currentWord
            #Taking the user input of their guessed words.
            guessWord = input("\n Guess Number {}:".format(numberOfUserGuesses))
            #Creating nested loop within while loop.
            for n in range(0, len(currentWord)):
            #If statement that determines if a letter is in the guessed word and also in the same place, print the letter green.
                if guessWord[n] == currentWord[n]:
                    print(termcolor.colored(guessWord[n], 'green'), end="")
            #States that if a letter in the guessword is also in the current word, but not in the same place, print as yellow.
                elif guessWord[n] in currentWord:
                    print(termcolor.colored(guessWord[n], 'yellow'), end="")
            #States that if there are no letters that are similar in the guess to the current word, print as grey.
                else:
                    print(termcolor.colored(guessWord[n], 'grey'), end="")
            #If the word is correctly guessed, print the following.
            if guessWord == currentWord:
                print("\n Congrats on getting today's wordle which was {}!You got it in {} tries".format(currentWord, numberOfUserGuesses))
                #Safely exiting the program.
                sys.exit("Thank you for playing wordle today!")
            #If the user runs out of guesses allowed, print the following.
            elif numberOfUserGuesses == numberOfGuessesAllowed:
                 print("\n You were not able to guess {} in {} tries. Try again!".format(currentWord, numberOfUserGuesses))
        #Safely exiting program.
        sys.exit("Thank you for playing wordle today!")


# Code that instantiates your wordle class and runs it
game = Wordle(6, "myWords.txt")
game.readFile()
game.selectRandomWord()
game.removeNewLineFromWord()
game.playWordle()
