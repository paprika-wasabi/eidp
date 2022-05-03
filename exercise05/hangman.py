# Importieren des Moduls für das generieren von Zufallszahlen
import random


def input_choice(answer: list, answer1: list) -> str:  # Aufgabenteil (a)
    answer = input("Do you want to play a game? [yes | no] \n")
    if answer == 'yes':
        return 'yes'
    elif answer == 'no':
        pass
    else:
        while answer1 != 'yes' and answer1 != 'no':
            answer1 = input("Invalid answer. Try again. \n")
        if answer1 == 'yes':
            return 'yes'
        elif answer1 == 'no':
            pass


def shape(word: str, guesses: str) -> str:  # Aufgabenteil (b)
    result = ""
    for char in word:
        if char in guesses:
            result += char
        else:
            result += "_"
    return result


def hangman(word: list, max_fails: int):  # Aufgabenteil (c)
    for char in word:
        print('_', end='')
    guesses = str(input(("; " + str(max_fails) + " mistakes left; " + "make a guess: ")))
    end = 0
    guessesletter = ""
    result = ""
    while max_fails != 1 and end == 0:
        result = ""
        if len(guesses) == 1 and result != word:
            if guesses in word:
                guessesletter += guesses
            elif guesses not in word:
                max_fails = max_fails - 1
            for char in word:
                if char in guessesletter:
                    result += char
                else:
                    result += "_"
        elif len(guesses) != 1:
            print("Invalid input. Guess has to be exactly one letter. Try again.")
            if guesses in word:
                pass
            elif guesses not in word:
                pass
            for char in word:
                if char in guessesletter:
                    result += char
                else:
                    result += "_"
        if result != word:
            print(result, end="")
            guesses = str(input(("; " + str(max_fails) + " mistakes left; " + "make a guess: ")))
        elif result == word:
            end = 1
    print()
    if result == word:
        print("You won! The word was " + "'" + word + "'" + " ! You're the best! Everyone loves you!")
    elif max_fails == 1 and result != word:
        print("You lose! The word was " + "'" + word + "'" + " ! You're the worst! Everyone hates you!")


if __name__ == '__main__':
    words = ['apple', 'tree', 'python', 'bench', 'float']

    max_fails = int(input("Number of allowed mistakes: "))

    while input_choice("Wanna play a game?", ['yes', 'no']) == 'yes':
        word = random.choice(words)  # Wähle ein zufälliges Wort aus.
        hangman(word, max_fails)