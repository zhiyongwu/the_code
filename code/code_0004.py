"""
任一个英文的纯文本文件，统计其中的单词出现的个数。
"""


def count(file):
    result = dict()
    with open(file, encoding='gbk') as f:
        for line in f:
            words = line.strip().split(" ")
            for word in words:
                if word in result.keys():
                    result[word] = result[word] + 1
                else:
                    result[word] = 1
    return result


if __name__ == '__main__':
    r = count('../text/1.txt')
    print(r['good'])
