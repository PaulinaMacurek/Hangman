import random


def check_input(usr_input):
    if len(usr_input) == 1:
        if usr_input.isalpha() and usr_input.islower():
            return True
        else:
            print('Please, enter a lowercase letter from the English alphabet.')
            return False
    else:
        print('Please, input a single letter.')
        return False


def hangman():
    words = ('java', 'python', 'swift', 'javascript')
    word = random.choice(words)
    word_lst_format = list("-" * (len(word)))
    counter = 8
    tries = set()
    while True:
        print('\n' + ''.join(word_lst_format))
        letter = input('Input a letter: ')
        if not check_input(letter):
            continue
        else:
            if letter in tries:
                print("You've already guessed this letter.")
                continue
            else:
                tries.add(letter)
                if (letter in word) and (letter not in word_lst_format):
                    table = [position for position, char in enumerate(word) if char == letter]
                    for x in table:
                        word_lst_format[x] = letter
                elif letter not in word:
                    print("That letter doesn't appear in the word.")
                    counter -= 1
                else:  # letter in word and letter in word_lst_format
                    print('No improvements.')
                    counter -= 1

            if '-' not in word_lst_format:
                print('\n' + ''.join(word_lst_format))
                print(f'You guessed the word {word}!')
                print('You survived!')
                return True
            elif counter == 0:
                print('You lost!')
                return False


nbr_wins = 0
nbr_lost = 0
print("H A N G M A N")
while True:
    msg = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if msg == 'play':
        if hangman():
            nbr_wins += 1
        else:
            nbr_lost += 1
    elif msg == 'results':
        print(f'You won: {nbr_wins} times.')
        print(f'You lost: {nbr_lost} times.')
    else:
        break
