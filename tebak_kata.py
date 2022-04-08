import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 5

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('kamu mempunyai', lives, 'kesempatan untuk hidup, silahkan pilih kata selanjutnya: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('kata nya adalah : ', ' '.join(word_list))

        user_letter = input('tebak 1 huruf lainnya: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nhuruf yang kamu pilih,', user_letter, 'tidak ada di kata hero')

        elif user_letter in used_letters:
            print('\nKata yang kamu pilih sudah ada, silahkan pilih kata lain')

        else:
            print('\nmaaf itu salah')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('maaf kamu kalah, hero nya adalah a', word)
    else:
        print('YAY! kata yang kamu pilih benar ', word, '!!')


if __name__ == '__main__':
    hangman()