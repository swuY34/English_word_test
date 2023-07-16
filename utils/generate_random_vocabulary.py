#  -*- coding: utf-8 -*-
"""
@Author        : swuY
@Time          : 2023/7/7 12:34
@FileName      : generate_random_vocabulary
@Editors       : PyCharm
"""

import json
import random

def generate_word() -> None:
    with open('data/db_of_vocabulary.json', 'r', encoding = 'utf-8') as file:
        data_dict = json.loads(file.read())
        data_list = []
        for data in data_dict.items():
            data_list.append(data)

    count_correct = 0
    count_failed = 0

    while 1:
        check_mode = random.randint(1, 4)
        word_pair = random.choice(data_list)
        if check_mode == 4:
            response = input(f'请输入对应单词的中文翻译 ({word_pair[0]}): ')
            if response == word_pair[1]:
                print('回答正确')
                count_correct += 1
            else:
                print(f'回答错误, 正确答案是: {word_pair[1]}')
                count_failed += 1

        if check_mode != 4:
            response = input(f'请输入对应单词的英文翻译 ({word_pair[1]}): ')
            if response == word_pair[0]:
                print('回答正确')
                count_correct += 1
            else:
                print(f'回答错误, 正确答案是 {word_pair[0]}')
                count_failed += 1

        print()

