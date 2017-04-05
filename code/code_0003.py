"""
将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
"""
import redis

from code.code_0001 import generate_200_code

r = redis.Redis('123.206.178.235')


def save(code_set):
    r.set("key", '\n'.join(code_set))


if __name__ == '__main__':
    save(generate_200_code())
