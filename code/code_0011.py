"""
 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
"""

filtered_words = list((line.strip() for line in open('../text/filtered_words.txt', encoding='utf-8')))


def is_filter_word(word):
    if word in filtered_words:
        return True
    for each in filtered_words:
        if each in word:
            return True
    return False


if __name__ == '__main__':
    while True:
        c_in = input()
        if is_filter_word(c_in):
            print("Freedom")
        else:
            print("Human Rights")
