from random import choice
from Stages import stages
from time import sleep
import turtle


guessed_letters = []

guessed_words = []

word_lst = ['opal', 'time', 'jobs', 'frog']

word = choice(word_lst)

tries = 6

word_completion = len(word) * '_'

word_complete = False

tries_gone = False


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
    print(f"You have >> {tries} << tries left!")
    sleep(0.75)
    print(word_completion)
    sleep(0.75)
    stages(tries)
    print(f"You have guessed the letters: {', '.join(guessed_letters)}")


def CheckGameOver():
    global word_complete
    global tries_gone

    if '_' not in word_completion:
        word_complete = True

    if tries < 1:
        tries_gone = True


def Won():
    print(f"Yay you guessed the word: {word}!!")


def Lost():
    print(f"Oh no you lost :( The word was {word} by the way.")


def Rules():
    print(f"You have {tries} tries.")
    print("You can guess a letter or a word.")
    print("Each time you guess wrong, the hangman will be drawn further.")
    print("It starts with:")
    for i in range(3):
        print(". . .")
        sleep(0.5)
    stages(tries)
    print(f"on {tries} tries")
    sleep(1)
    print(f"Once all {tries} tries are gone, you lose.")


def main():
    global tries
    global is_running
    global word_completion

    is_running = True

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
                    print("Correct")
                    ReplaceWord(word_guess)
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

    turtle.bye()


if __name__ == '__main__':
    main()
