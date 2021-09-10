#Title: The Hangman V0.1
#Author: Diego Faria
#Date: 09/05/2020
import json
from colorama import init, Fore, Back, Style
import random
from Class.translate import translate

init() #Inits Colorama

#Step 1: Ask for a name
print(Style.BRIGHT + Fore.CYAN + "### H A N G M A N ###\nWritten by: Diego F.\n" + Style.RESET_ALL) #Title of the game
name = input("Please input your name: ") #Asks for a name that will be printed
while(True):
    print("Hello " + name.title() + "!") #Prints the name to greet

    #Step 2: Load the data and add the give name to it.
    data = json.load(open("data.json")) #Loads the data
    data[name] = "Your name. Your family gave it to you." #Add the given name to the data

    #Step 3:Pick a random word from the data that DOES NOT have spaces and has five chars or more
    keys = list(data.keys())
    while True:
        number = random.randrange(0, len(keys))
        word = keys[number].lower()

        if " " in word or len(word) < 5 or "-" in word:
            continue
        else:
            break

    #Step 4: While running, guess the word
    chars = {}
    for char in word:
        chars[char] = False

    run = True

    tries = 9
    while run:
        guess = ""
    
        for char in word:
            if chars[char] == True:
                guess += " " + char
            else:
                guess += " _"
            
        print(Style.BRIGHT + Fore.GREEN + "Guess the word:" + guess + "\n" + Style.RESET_ALL)

        if "_" not in guess:
            print(Style.BRIGHT + Fore.GREEN + "Congratulations! You won!" + Style.RESET_ALL)
            run = False
            continue

        #Print the hangman
        hangman = ""
        if tries != 9:
            if tries <= 8:
                hangman += "-----\n"

            if tries <= 7 and tries != 1 and tries != 0:
                hangman += " O   \n"
            elif tries == 1:
                hangman += " O_  \n"
            elif tries == 0:
                hangman += " O_|\n"

            if tries == 6:
                hangman += "/"

            if tries == 5:
                hangman += "/  \\"

            if tries <= 4:
                hangman += "/|\\  \n"

            if tries == 3:
                hangman += "/"

            if tries <= 2:
                hangman += "/ \\ \n"
        
        print(hangman)
        if tries == 0:
            print("Oh no! You lose!")
            run = False
            continue

        char_guess = ""
        while True:
            char_guess = str(input("Please pass in a letter (if you pass in more than one letter, only the first one will be checked): "))
            try:
                char_guess = char_guess[0].lower()
            except:
                print(Style.BRIGHT + Fore.RED + "Do not pass in an empty string!" +Style.RESET_ALL)
                continue

            if char_guess == " " or char_guess == "-":
                print(Style.BRIGHT + Fore.RED + "No Spaces or guions. Try again." + Style.RESET_ALL)
                continue
            else:
                break
                
        if char_guess in word:
            if chars[char_guess] == True:
                print(Style.BRIGHT + Fore.RED + "You already put this letter!\n" + Style.RESET_ALL)
            else:
                chars[char_guess] = True
        else:
            print(Style.BRIGHT + Fore.RED + "Wrong letter!")
            tries = tries - 1
            print("Remaining attempts: " + str(tries) + Style.RESET_ALL)

    print("The word is: " + Style.BRIGHT + Fore.CYAN +  word + Style.RESET_ALL + "\n")
    print("It means: ")
    translate(word, data)

    c = input("If you want to play again, input 0 to end the program, otherwise input something different: ")
    if(c == '0'):
        break
    else:
        continue