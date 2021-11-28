from random import choice
from Stages import stages
from time import sleep


guessed_letters = []

word_lst = ['opal', 'time', 'jobs', 'frog']

word = choice(word_lst)

tries = 6

word_completion = len(word) * '_'


def ReplaceChar(letter_guess, word=word):
    global word_completion

    guess_positions = [idx for idx, letter in enumerate(word) if letter in letter_guess]
    word_completion_long = list(word_completion)
    if guess_positions:
        for idx in guess_positions:
            word_completion_long[idx] = letter_guess
    word_completion = "".join(word_completion_long)


def EndofTurn():
    print(f"You have >> {tries} << tries left!")
    sleep(0.75)
    print(word_completion)
    sleep(0.75)
    stages(tries)


def main():
    global tries

    is_running = True

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

    if '_' in word_completion:

        form = input("Would you like to guess a word or letter? (w or l) ")

        if form == 'l':
            letter_guess = input("What letter would you like to guess? (lower case) ")

            if letter_guess in word:
                print("Correct!")
                ReplaceChar(letter_guess)
                EndofTurn()

            else:
                print("Wrong!")
                sleep(0.5)
                tries -= 1
                EndofTurn()

        elif form == 'w':
            word_guess = input("What word you like to guess? (all lower case) ")

            if word_guess == word:
                print("Correct")
                tries -= 6

            else:
                print("Wrong!")
                tries -= 1
                EndofTurn()

        else:
            'Enter a vail letter!'

    elif tries > 0:
        "Oh no! You ran out of tries... you lost :("

    else:
        print("YAY you won!")


if __name__ == '__main__':
    main()
