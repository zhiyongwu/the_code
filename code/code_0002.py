"""
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
"""
import pymysql

from code.code_0001 import generate_200_code

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
    'database': 'data'
}

conn = pymysql.connect(**config)


def insert_code(code):
    cur = conn.cursor()
    sql = "insert into code_save (code) VALUES ('%s')" % code
    cur.execute(sql)


if __name__ == '__main__':
    all_code = generate_200_code()
    for each in all_code:
        insert_code(each)
    conn.commit()
    conn.close()
