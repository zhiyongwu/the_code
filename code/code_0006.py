"""
你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
"""
from code import code_0004


def get_important_word(file):
    result = code_0004.count(file)
    num = 0
    w = None
    for word, count in result.items():
        if count > num:
            num = count
            w = word
        else:
            pass
    return w, num


if __name__ == '__main__':
    print(get_important_word('../text/4.txt'))
