from random import choice
from Stages import stages
from time import sleep
import turtle
import sys


guessed_letters = []

guessed_words = []

tries = 6

word_complete = False

tries_gone = False


def SetScreen():
    stages(100)
    print("Hello! This will be your screen throughout the game")
    sleep(1)
    print("Please wait for the game to begin")
    sleep(2)


def GetWord():
    global word

    categories = ["fruits and vegetables", "countries", "animals", "extended countries"]

    print("First you need to choose the category your word will be!")
    sleep(1)
    print("The catergories are:")
    for idx, cat in enumerate(categories):
        print(f"{cat}: {idx + 1}")
        sleep(0.5)

    category = int(input("What category would you like to choose? (1 - 4) "))

    if category == 1:
        with open("WordCategories/fruits_vegetables.txt", "r") as f:
            words = f.read()
            word_lst = words.split("\n")
            del word_lst[-1]

    elif category == 2:
        with open("WordCategories/countries.txt", "r") as c:
            words = c.read()
            word_lst = words.split("\n")
            del word_lst[-1]

    elif category == 3:
        with open("WordCategories/animals.txt", "r") as a:
            words = a.read()
            word_lst = words.split("\n")
            del word_lst[-1]

    elif category == 4:
        with open("WordCategories/countries_extended.txt", "r") as a:
            words = a.read()
            word_list = words.split("\n")
            word_lst = [x.lower() for x in word_list]
            del word_lst[-1]

    else:
        print("Please enter a valid number")
        sys.exit()

    word = choice(word_lst)

    print(f"Your word is {len(word)} characters long")

    sleep(1)

    return word


GetWord()
word_completion = len(word) * '_'


def ReplaceChar(letter_guess, word=word):
    global word_completion

    guess_positions = [idx for idx, letter in enumerate(word) if letter in letter_guess]
    word_completion_long = list(word_completion)
    if guess_positions:
        for idx in guess_positions:
            word_completion_long[idx] = letter_guess
    word_completion = "".join(word_completion_long)


def ReplaceWord(word_guess, word=word):
    global word_completion

    word_completion = word


def EndofTurn():
    if tries == 1:
        print(f"You have >> {tries} << try left!")
    elif tries > 1:
        print(f"You have >> {tries} << tries left!")
    sleep(0.75)
    print(word_completion)
    sleep(0.5)
    stages(tries)
    print(f"You have guessed the letters: {', '.join(guessed_letters)}")


def CheckGameOver():
    global tries
    global word_complete
    global tries_gone

    if '_' not in word_completion:
        word_complete = True
        tries = 0

    if tries < 1:
        tries_gone = True


def Won():
    print(f"Yay you guessed the word: {word}!!")
    sleep(2)
    sys.exit()


def Lost():
    print(f"Oh no you lost :( The word was {word} by the way.")
    sleep(2)
    sys.exit()


def Rules():
    print(f"You have {tries} tries.")
    sleep(1)
    print("You can guess a letter or a word.")
    sleep(1)
    print("Each time you guess wrong, the hangman will be drawn further.")
    sleep(1)
    print(f"Once all {tries} tries are gone, the hangman is completed and you LOSE!")


def main():
    global tries
    global is_running
    global word_completion

    is_running = True

    SetScreen()

    Rules()

    while not word_complete and not tries_gone:

        CheckGameOver()

        if word_complete:
            Won()
            break

        if tries_gone:
            Lost()
            break

        form = input("Would you like to guess a word or letter? (w or l) ")

        if form == 'l':
            letter_guess = input("What letter would you like to guess? (lower case) ")

            if letter_guess not in guessed_letters:

                guessed_letters.append(letter_guess)

                if letter_guess in word:
                    print("Correct!")
                    ReplaceChar(letter_guess)
                    CheckGameOver()

                    if word_complete:
                        Won()
                        break

                    if tries_gone:
                        Lost()
                        break

                    EndofTurn()
                    continue

                else:
                    print("Wrong!")
                    sleep(0.5)
                    tries -= 1
                    EndofTurn()
                    continue

            else:
                print("You have already entered this letter... please enter a new letter")
                continue

        elif form == 'w':
            word_guess = input("What word you like to guess? (all lower case) ")

            if word_guess not in guessed_words:

                guessed_words.append(word_guess)

                if word_guess == word:
                    print("Correct!")
                    ReplaceWord(word_guess)
                    CheckGameOver()
                    if word_complete:
                        Won()
                        break

                    if tries_gone:
                        Lost()
                        break
                    EndofTurn()
                    continue

                else:
                    print("Wrong!")
                    tries -= 1
                    EndofTurn()
                    continue
            else:
                print("You have already entered this word... please enter a new word")
                continue

        else:
            'Enter a valid form (l for letter or w for word)!'
            continue


if __name__ == '__main__':
    main()

turtle.done()
