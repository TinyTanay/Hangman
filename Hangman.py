import random

global word_lst
HANGMANPICS = [
    '''''',
    '''
      
=========''',
    '''
      |
      |
      |
      |
      |
========='''
    , '''
  +---+
  |   |
      |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

alphabet = 'abcdefghijklmnopqrstuvwxyz'
guessed = []

with open("wordlist.txt", "r") as f:
    words = f.read()
    word_lst = words.split("\n")


def get_word(word_lst):
    word = random.choice(word_lst)
    return word


def replace_char(string, charNumber, char):
    temp = list(string)
    temp[charNumber] = char
    return "".join(temp)


def check_correct(currentValue, targetValue):
    return currentValue == targetValue


def play(word):
    current = '_' * len(word)
    fails = 0
    while '_' in current:
        character = input("Guess! ")
        if len(character) > 1 or len(character) < 1:
            print('Enter a character!')
            continue
        if character not in alphabet:
            print('Enter a valid english letter!')
            continue
        count = 0
        hasFailed = True
        if character in guessed:
            print('You have already guessed that!')
            continue
        guessed.append(character)
        for c in word:
            if c == character:
                current = replace_char(current, count, c)
                if check_correct(current, word):
                    print('You win!')
                    return
                print(current)
                hasFailed = False
                count += 1
                continue
            else:
                count += 1
                continue
        if hasFailed:
            fails += 1
            print(HANGMANPICS[fails])
            if fails == 9:
                print('Hanged! The word was ' + word)
                return


play(get_word(word_lst))
    
