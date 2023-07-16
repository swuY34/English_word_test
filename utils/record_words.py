#  -*- coding: utf-8 -*-
"""
@Author        : swuY
@Time          : 2023/7/16 15:58
@FileName      : record_words
@Editors       : PyCharm
"""

import json

def record_words(
    words_list: str, translate_words_list: str
) -> None:
    with open('data/db_of_vocabulary.json', 'r', encoding='utf-8') as file:
        original_data = json.loads(file.read())

    for word, translate_word in zip(words_list.split(', '), translate_words_list.split(', ')):
        new_data = {word: translate_word}
        original_data.update(new_data)

    with open('data/db_of_vocabulary.json', 'w', encoding='utf-8') as file:
        json.dump(original_data, file, indent = 4)
