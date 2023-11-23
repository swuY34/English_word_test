#  -*- coding: utf-8 -*-
"""
@Author        : swuY
@Time          : 2023/7/17 18:01
@FileName      : text_to_list
@Editors       : PyCharm
"""

"""
# this is style of the parameter
x = '''abandon
ability
able
abnormal
aboard
abolish
abortion
about
above
abroad
abrupt'''
# you can change the parameter here
"""

def text_to_list(
        original_string: str, original_string_translated: str
) -> tuple[str]:
    words_list = str(original_string.split('\n')).replace("'", '').replace('[', '').replace(']', '')
    words_translated_list = str(original_string_translated.split('\n')).replace("'", '').replace('[', '').replace(']', '')

    return words_list, words_translated_list

parameter = '''argument
boil
catch
ceremony
convenience
dangerous
dialogue
during
expression
fair
fruit
graduate
hilly
hometown
master
nutrition
painting
personnel
private
quiz
relative
reserve
sister-in-law
snowball
system
third
time
variety
withdraw
worth'''

parameter1 = '''争论
沸腾
接
仪式
方便
危险
对话
期间
表达
公平
果实
毕业
丘陵
家乡
硕士
营养学
绘画
人事
私人
测验
亲属
后备
嫂子
雪球
系统
第三次
时间
品种
退出
价值'''

if __name__ == '__main__':
    result_words_english, result_words_chinese = text_to_list(parameter, parameter1)
    print(result_words_english)
    print(result_words_chinese)
