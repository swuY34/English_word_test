#  -*- coding: utf-8 -*-
"""
@Author        : swuY
@Time          : 2023/7/17 17:32
@FileName      : random_new_words
@Editors       : PyCharm
"""

import json
import random

with open('../data/3500words.txt', 'r', encoding='utf-8') as f:
    all_data = f.readlines()
    final_data_list = []

    # 随机出新单词
    all_data = [data.replace('\n', '') for data in all_data]
    new_words = []

    for i in range(int(input('要几个单词: '))):
        all_data_length = len(all_data)
        new_word_id = random.randint(0, all_data_length - 1)
        new_word = all_data[new_word_id]
        del all_data[new_word_id]

        new_words.append(new_word)

    for word in sorted(new_words):
        print(word)

with open(r'../data/3500words.txt', 'w', encoding='utf-8') as f:
    x = '\n'
    f.write(x.join(all_data))
