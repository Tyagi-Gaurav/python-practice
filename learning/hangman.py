#!/usr/bin/python3

import random
import hangman_words

stages = [[
        "    +----+",
        "    |    |",
        "    O    |",
        "         |",
        "         |",
        "         |",
        "============="
            ],[
        "    +----+",
        "    |    |",
        "    O    |",
        "    |    |",
        "         |",
        "         |",
        "============="
            ],
            [
        "    +----+",
        "    |    |",
        "    O    |",
        "  / |    |",
        "         |",
        "         |",
        "============="
            ],
            [
        "    +----+",
        "    |    |",
        "    O    |",
        "  / | \  |",
        "         |",
        "         |",
        "============="
            ],
            [
        "    +----+",
        "    |    |",
        "    O    |",
        "  / | \  |",
        "   /     |",
        "         |",
        "============="
            ],[
        "    +----+",
        "    |    |",
        "    O    |",
        "  / | \  |",
        "   / \   |",
        "         |",
        "============="]]

def show_hangman(number_of_lives):
    for stage in stages[len(stages) - number_of_lives]:
        print (stage)

def show_display(display):
    display_str = ''
    for ch in display:
        display_str += ch

    print (display_str)

end_of_game = False

number_of_lives = 6
chosen_word = random.choice(hangman_words.word_list)

display = []
for _ in range(len(chosen_word)):
    display += '-'

while not end_of_game:
    show_hangman(number_of_lives)
    print("\n")
    show_display(display)
    print("\n")

    guess=input("Guess the letter? ").lower()
    if guess in display:
        print ("You have already guessed " + guess)
    else:
        if guess in chosen_word:
            for pos in range(len(chosen_word)):
                if chosen_word[pos] == guess:
                    display[pos] = guess
            
            if '-' not in display:
                print (display)
                end_of_game = True
                print ("You win!")
        else:
            print ("You guessed " + guess + ", that's not in the word. You lose a life.") #Draw hangman
            number_of_lives -=1
            if number_of_lives == 1:
                end_of_game = True
                print ("You lose!. The word was " + chosen_word)
