import random
from art import stages
from art import word_list
from art import logo
import os

def game():
    gameover = False
    lives = 6
    rand_word = random.choice(word_list)
    letters_used = []
    # Creating the blanks
    check_win = []
    for l in range(len(rand_word)):
        check_win += "_"
 
    while not gameover: 
        os.system('cls')
        print(logo)
        print(stages[lives])
        print(f"Letters already used: {' '.join(letters_used)}\n")
        #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(check_win)}\n")
        guess = input("Choose a letter to see if it's in the word: ").lower()
        letters_used += guess
        
        
        #Check if the letter is in the word
        for l in range(len(rand_word)):
            letter = rand_word[l]
            if letter == guess:
                check_win[l] = letter   
        if guess not in check_win:
            lives -= 1

        if "_" not in check_win:
            gameover = True
            print("You got it!")
            if input(" Play again? Y/N: ").lower() == "y":
                print("let's go")
                game()
            else:
                print("Thanks for playing!")
                gameover = True
        if lives == 0:
            os.system('cls')
            print(logo)
            print(f"{stages[0]}\n You lost. The word was {rand_word}\n")
            if input(" Play again? Y/N: ").lower() == "y":
                print("let's go")
                game()
            else:
                print("Thanks for playing!")
                gameover = True

game()
