#  -*- coding: utf-8 -*-
"""
@Author        : swuY
@Time          : 2023/7/16 16:00
@FileName      : main
@Editors       : PyCharm
"""

from utils import generate_random_vocabulary
from utils import record_words

def main():
    while 1:
        option = input('\noption 1 -> practice\noption 2 -> record words\n\nenter your option(1/2/exit): ')
        print()
        if option == '1':
            generate_random_vocabulary.generate_word()
        elif option == '2':
            words_list = input('enter your words(english) -> form (word, word....): ')
            translate_words_list = input('enter your translate words(chinese) -> form (word, word....): ')
            record_words.record_words(words_list, translate_words_list)
        elif option == 'exit':
            exit()
        else:
            print('value Error')
            continue

if __name__ == '__main__':
    main()
