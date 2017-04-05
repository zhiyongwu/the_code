"""
敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""
filtered_words = [word.strip() for word in open('../text/filtered_words.txt', encoding='utf-8')]


def filter_word(word):
    for each in filtered_words:
        if each in word:
            word = word.replace(each, '*' * len(each))
    return word


if __name__ == '__main__':
    while True:
        c_in = input()
        print(filter_word(c_in))
