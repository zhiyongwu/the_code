"""
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
code_len = 16
"""
import string, random

result_set = set()


def generate_code():
    all_letters = string.ascii_letters + string.digits
    code = []
    for x in range(16):
        code.append(random.choice(all_letters))
    return ''.join(code)


def generate_code_limit(num):
    while len(result_set) < num:
        result_set.add(generate_code())


def generate_200_code():
    generate_code_limit(200)
    return result_set

if __name__ == '__main__':
    while len(result_set) < 200:
        result_set.add(generate_code())
    print('\n'.join(result_set))
